import paho.mqtt.client as mqtt
import keyboard
import json
import time

address = "2939d3617acc492aa3b3653ac474fdc0.s2.eu.hivemq.cloud" # Pull Request comment 1: Address van broker. Dit is belangrijk, want anders kan je niet connecten.
port = 8883 # Pull Request comment 1: Port van broker. Dit hoort bij de address. Ook belangrijk voor connectie.

# Pull Request comment 1: MQTT topic naam om naar te publishen, en subscribers kunnen subscriben op deze topic om de data te ontvangen
topic_1 = "inputs/cabinEmergencyButton"
topic = "inputs/joystick"

# Pull Request comment 1: MQTT client aanmaken (in een variable gezet) om later mee te connecten
client = mqtt.Client()

# Pull Request comment 1: Callback functie voor als de client verbonden is met de broker. De RC parameter (Return Code) geeft aan of de connectie succesvol is of niet.
# Pull Request comment 1: properties=None is een extra parameter die we niet gebruiken, maar wel moeten meegeven, anders maaktie geen connectie (ik had gisteren hier uren aan verspild).
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected to broker")
    else:
        print(f"Connection failed with code {rc}")
        
def on_message(client, userdata,message):
        print("Message received: " + str((message.payload.decode("utf-8"))))
        print("Topic is " + str(message.topic))
  
         
  # decodes the JSON and allows us to get the values of the movement, speed and lock.
        payload_data = json.loads(message.payload.decode('utf-8'))
        movement = payload_data.get("movement") # The movement of the joystick input
        speed = payload_data.get("speed") # Speed from joystick input, we will adjust this in our payload
        lock = payload_data.get("lock") # Checks whether spreader is locked or not
        emergency = payload_data.get("emergency") # Checks for emergency from the inputs/cabinEmergencyButton
        print("payload data",payload_data)

        try:
            # if data received from inputs/joystick and emergency is false
            if message.topic == topic and emergency is False:
                movement =  movement
                speed = speed
                lock = lock
                emergency = False
                print("MESSAGE TOPIC is " + topic + " and emergency is set to", emergency )
            # if data received from inputs/joystick and emergency is true    
            elif message.topic == topic and emergency is True:
                movement =  movement
                speed = speed
                lock = lock
                emergency = True
                print("MESSAGE TOPIC is " + topic + " and emergency is set to", emergency )
            else:
                print ("error trying to get data from " + topic)
            # payload that we send to outputs/cabinEmergencyButton    
            payload = {"movement": movement, "speed": speed, "lock": lock, "emergency": emergency}
            payload_string = json.dumps(payload)
            client.publish(topic_1, payload_string, qos=0)
            print("payload sent from emergencybutton", payload)
        except Exception as e:
            print("error", e)

            
client.on_connect = on_connect
client.on_message = on_message

# Pull Request comment 1: TLS (required for connection) - Dit was ook blijkbaar nodig voor de connectie, ook uren aan verspild. TLS zorgt voor een beveiligde connectie.
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# Username and password (required for connection)
client.username_pw_set("Admin", "hMu4P6L_LAMj8t3")


connected= False
messageReceived= False

# Main Loop
client.connect(address, port)
client.subscribe("inputs/joystick")
client.loop_start()

while connected!= True:
    time.sleep(0.2)
while messageReceived!= True: 
    time.sleep(0.2)
client.loop_forever()    

   