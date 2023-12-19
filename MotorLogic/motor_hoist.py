import ssl
import paho.mqtt.client as mqtt
import time
import json
from datetime import datetime

# connects us to the MQTT client
client = mqtt.Client()

# topics that we are subscribed to
topic_input_joystick = "inputs/joystick"
topic_input_cabinEmergencyButton = "inputs/cabinEmergencyButton"    
# topics that we publish our data to
topic_output_motorHoist = "outputs/motorHoist"
topic_logger_error = "logger/errors"

emergency = False


def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected to broker")
    else:
        print(f"Connection failed with code {rc}")

# prints back the message received and the topic
def on_message(client, userdata,message):
    if message.topic == topic_input_cabinEmergencyButton: # checks for topic
     print("Message received: " + str((message.payload.decode("utf-8"))))
     print("Topic is " + str(message.topic))
     payload_data = json.loads(message.payload.decode('utf-8'))
     global emergency
     emergency = payload_data.get("state")
    else: 
     print("Message received is " + str((message.payload.decode("utf-8"))))
     print("Topic is " + str(message.topic))
     payload_data = json.loads(message.payload.decode('utf-8'))
     movement = payload_data.get("movement") # The movement of the joystick input
     speed = payload_data.get("speed") # Speed from joystick input, we will adjust this in our payload

    # decodes the JSON and allows us to get the values of the movement, speed and lock.
    motorDirection = ""

    try:  
        if message.topic == topic_input_joystick and emergency is True:
            motorDirection = "none"
            current_datetime_utc = datetime.utcnow()
            formatted_datetime = current_datetime_utc.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            publish_payload(topic_logger_error, {"EventTimeStamp":formatted_datetime,"EventType":"Error","Component":"Hoist motor","Description":"Hoist motor cant move since emergency button is engaged!"})
            publish_payload(topic_output_motorHoist, {"direction": motorDirection, "speed": "none"})
        elif message.topic == topic_input_joystick and emergency is False :  # only does actions if its from inputs/joystick and emergency is false
            if movement == "none" :
                motorDirection = "none"
                publish_payload(topic_output_motorHoist, {"direction": motorDirection, "speed": "none"})
            if speed == 'normal': # normal speed
                # Up and down are for the Hoist movements
                if movement == "up":
                    motorDirection = "clockwise"
                    publish_payload(topic_output_motorHoist, {"direction": motorDirection, "speed": speed})
                elif movement == "down":    
                    motorDirection = "antiClockwise"
                    publish_payload(topic_output_motorHoist, {"direction": motorDirection, "speed": speed})
                    
            # For fast speed
            elif speed == 'fast':
                if movement == "up":
                    motorDirection = "clockwise"
                    publish_payload(topic_output_motorHoist, {"direction": motorDirection, "speed": speed})
                elif movement == "down":    
                    motorDirection = "antiClockwise"
                    publish_payload(topic_output_motorHoist, {"direction": motorDirection, "speed": speed})

            # For slow speed      
            elif speed == 'slow':   
            # Up and down are for the Hoist movements
                if movement == "up":
                    motorDirection = "clockwise"
                    publish_payload(topic_output_motorHoist, {"direction": motorDirection, "speed": speed})
                elif movement == "down":    
                    motorDirection = "antiClockwise"
                    publish_payload(topic_output_motorHoist, {"direction": motorDirection, "speed": speed})
                       
            else: # if Emergency is true this will happen
              print("Emergency button has activated ")
       

    except Exception as e:
        print("Error:", e)

def publish_payload(topic,payload):{
    
    client.publish(topic, json.dumps(payload))

} 

connected= False
messageReceived= False

# HiveMQ URL and port for connection
broker = "2939d3617acc492aa3b3653ac474fdc0.s2.eu.hivemq.cloud"
port = 8883
username = "Admin"
password = "hMu4P6L_LAMj8t3"

# TLS (required for connection)
client.tls_set(cert_reqs=mqtt.ssl.CERT_NONE)

# Username and password (required for connection)
client.username_pw_set(username, password)

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)
client.subscribe(topic_input_joystick) ## have to be subscribed first then client_loop start!
client.loop_start()

while connected!= True:
    time.sleep(0.2)
while messageReceived!= True: 
    time.sleep(0.2)

client.loop_forever()    
