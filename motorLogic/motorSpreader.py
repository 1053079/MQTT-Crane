import paho.mqtt.client as mqtt
import time
import json

# connects us to the MQTT client
client = mqtt.Client()

# topics that we are subscribed to
topic = "inputs/joystick"
topic_1 = "inputs/cabinEmergencyButton"

# topics that we publish our data to
topic_2 = "outputs/motorSpreader"

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected to broker")
    else:
        print(f"Connection failed with code {rc}")

# prints back the message received and the topic
def on_message(client, userdata,message):
    print("Message received: " + str((message.payload.decode("utf-8"))))
    print("Topic is " + str(message.topic))
    
    # decodes the JSON and allows us to get the values of the movement, speed and lock.
    payload_data = json.loads(message.payload.decode('utf-8'))
    movement = payload_data.get("movement") # The movement of the joystick input
    speed = payload_data.get("speed") # Speed from joystick input, we will adjust this in our payload
    lock = payload_data.get("lock") # Checks whether spreader is locked or not
    emergency = payload_data.get("emergency") # Checks for emergency from the inputs/cabinEmergencyButton

    try:  
       if payload_data: # only does actions if we receive payload data from inputs/joystick
        if not emergency: # only does actions if emergency is set to false
         if speed == 'normal': # normal speed
          #  Spreader lock and unlock
          if movement == "none":
             print("Spreader is unlocked / locked ")
          else:
             print("invalid key detected")      

        #  for fast speed
         elif speed == 'fast':
          # Spreader lock and unlock
          if movement == "none":
              print("Spreader is unlocked / locked")
          else:
              print("invalid key detected")  

        # for slow speed      
         elif speed == 'slow':   
          #  Spreader lock and unlock    
          if movement == "none":
              print("Crane lock is unlocked / locked" )     
          else:
              print("invalid key detected")  
                     
         else: # if Emergency is true this will happen
              print("Emergency button has activated")
       
        # Payload that we send to topic_2 which is output/motorCabin
         payload_2 = {"movement": movement, "speed": speed, "lock": lock}
         print("payload is " , payload_2) 
         payload_string = json.dumps(payload_2)
         client.publish(topic_2, payload_string, qos=0)

    except Exception as e:
        print("Error:", e)
    

connected= False
messageReceived= False

# HiveMQ URL and port for connection
broker = "2939d3617acc492aa3b3653ac474fdc0.s2.eu.hivemq.cloud"
port = 8883
username = "Admin"
password = "hMu4P6L_LAMj8t3"

# TLS (required for connection)
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# Username and password (required for connection)
client.username_pw_set(username, password)

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)
client.subscribe(topic) ## have to be subscribed first then client_loop start!
client.loop_start()

while connected!= True:
    time.sleep(0.2)
while messageReceived!= True: 
    time.sleep(0.2)

client.loop_forever()    
