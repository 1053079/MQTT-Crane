
import paho.mqtt.client as mqtt
import time
import json


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
    movement = payload_data.get("movement")
    speed = payload_data.get("speed")
    lock = payload_data.get("lock")
    

    try:  
      if payload_data: 
       if not lock: ## if lock is not on we will perform these actions
        if speed == 2 : ## normal speed
         ## Forward and backward are for the Cabin movements
         if movement == "forward":  
              print("You have pressed " + movement + " at cabinspeed 2")
         elif movement == "backward":
              print("You have pressed " + movement + " at cabinspeed 2")
         ## Left and right are for the Crane movements 
         elif movement == "left":
              print("You have pressed " + movement + " at cranespeed 2")
         elif movement == "right":
              print("You have pressed " + movement + " at cranespeed 2")
          ## Up and down are for the Hoist movements
         elif movement == "up":
             print("You have pressed " + movement + " at hoistspeed 2")
         elif movement == "down":    
             print("You have pressed " + movement + " at hoistspeed 2")
         elif movement == "none":
             print("Crane has stopped")    
         else:
             print("invalid key detected")      

        ## for fast speed
        elif speed == 3:
        ## Forward and backward are for the Cabin movements
         if movement == "forward":  
             print("You have pressed " + movement + " at cabinspeed 3")
         elif movement == "backward":
             print("You have pressed " + movement + " at cabinspeed 3")

         ## Left and right are for the Crane movements 
         elif movement == "left":
             print("You have pressed " + movement + " at cranespeed 3")
         elif movement == "right":
             print("You have pressed " + movement + " at cranespeed 3")
             

          ## Up and down are for the Hoist movements
         elif movement == "up":
              print("You have pressed " + movement + " at hoistspeed 3")
         elif movement == "down":    
              print("You have pressed " + movement + " at hoistspeed 3")
         elif movement == "none":
              print("Crane has stopped")  
         else:
              print("invalid key detected")  

        ## for slow speed      
        elif speed == 1:   
         ## Forward and backward are for the Cabin movements
         if movement == "forward":  
              print("You have pressed " + movement + " at cabinspeed 1")
         elif movement == "backward":
              print("You have pressed " + movement + " at cabinspeed 1")

         ## Left and right are for the Crane movements 
         elif movement == "left":
             print("You have pressed " + movement + " at cranespeed 1")
         elif movement == "right":
             print("You have pressed " + movement + " at cranespeed 1")
             
          ## Up and down are for the Hoist movements
         elif movement == "up":
              print("You have pressed " + movement + " at hoistspeed 1") 
         elif movement == "down":    
              print("You have pressed " + movement + " at hoistspeed 1")
         elif movement == "none":
             print("Crane has stopped")  
         else:
             print("invalid key detected")         
        else:
         print("There was an error trying to get " + movement + " key")

    except Exception as e:
        print("Error:", e)
    
connected= False
messageReceived= False

# hiveMQ URL and port for connection
broker = "2939d3617acc492aa3b3653ac474fdc0.s2.eu.hivemq.cloud"
port = 8883
username = "Admin"
password = "hMu4P6L_LAMj8t3"

client = mqtt.Client()

# TLS (required for connection)
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# Username and password (required for connection)
client.username_pw_set(username, password)

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)
client.subscribe("output/motorCabin")
client.loop_start()

while connected!= True:
    time.sleep(0.2)
while messageReceived!= True: 
    time.sleep(0.2)

client.loop_forever()    
