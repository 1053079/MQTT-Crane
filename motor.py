import paho.mqtt.client as mqtt
import time
import json

# connects us to the MQTT client
client = mqtt.Client()

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
    movement = payload_data.get("movement") ## the movement of the joystick input
    speed = payload_data.get("speed") ## speed from joystick input, we will adjust this in our payload
    lock = payload_data.get("lock") ## Checks whether motor is locked or not
     
    # topics that we send data to
    topic_2 = "output/motorCabin"

    try:  
      if payload_data: ## only does actions if we receive payload data from inputs/joystick
       if not lock: ## if lock is not on we will perform these actions
        if speed == 'normal': ## normal speed
         ## Forward and backward are for the Cabin movements
         if movement == "forward":  
              print("You have pressed " + movement + " at " + speed + " speed")
              speed = 2
         elif movement == "backward":
              print("You have pressed " + movement + " at " + speed + " speed")
              speed = 2

         ## Left and right are for the Crane movements 
         elif movement == "left":
              print("You have pressed " + movement + " at " + speed + " speed")
              speed = 2
         elif movement == "right":
              print("You have pressed " + movement + " at " + speed + " speed")
              speed = 2

          ## Up and down are for the Hoist movements
         elif movement == "up":
              print("You have pressed " + movement + " at " + speed + " speed") 
              speed = 2
         elif movement == "down":    
              print("You have pressed " + movement + " at " + speed + " speed") 
              speed = 2
         else:
             print("invalid key detected")      

        ## for fast speed
        elif speed == 'fast':
        ## Forward and backward are for the Cabin movements
         if movement == "forward":  
              print("You have pressed " + movement + " at " + speed + " speed")
              speed = 3
         elif movement == "backward":
              print("You have pressed " + movement + " at " + speed + " speed")
              speed = 3

         ## Left and right are for the Crane movements 
         elif movement == "left":
              print("You have pressed " + movement + " at " + speed + " speed")
              speed = 3
         elif movement == "right":
              print("You have pressed " + movement + " at " + speed + " speed")
              speed = 3

          ## Up and down are for the Hoist movements
         elif movement == "up":
              print("You have pressed " + movement + " at " + speed + " speed") 
              speed = 3
         elif movement == "down":    
              print("You have pressed " + movement + " at " + speed + " speed") 
              speed = 3
         else:
             print("invalid key detected")  

        ## for slow speed      
        elif speed == 'slow':   
         ## Forward and backward are for the Cabin movements
         if movement == "forward":  
              print("You have pressed " + movement + " at " + speed + " speed")
              speed = 1
         elif movement == "backward":
              print("You have pressed " + movement + " at " + speed + " speed")
              speed = 1

         ## Left and right are for the Crane movements 
         elif movement == "left":
              print("You have pressed " + movement + " at " + speed + " speed")
              speed = 1
         elif movement == "right":
              print("You have pressed " + movement + " at " + speed + " speed")
              speed = 1

          ## Up and down are for the Hoist movements
         elif movement == "up":
              print("You have pressed " + movement + " at " + speed + " speed") 
              speed = 1
         elif movement == "down":    
              print("You have pressed " + movement + " at " + speed + " speed") 
              speed = 1
         else:
             print("invalid key detected")         
        else:
         print("There was an error trying to get " + movement)

        # Payload that we send to topic_2 which is output/motorCabin
        payload_2 = {"movement": movement, "speed": speed, "lock": lock}
        payload_string = json.dumps(payload_2)
        client.publish(topic_2, payload_string, qos=0)
        print(payload_2) 

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
client.subscribe("inputs/joystick") ## have to be subscribed first then client_loop start!
client.loop_start()

while connected!= True:
    time.sleep(0.2)
while messageReceived!= True: 
    time.sleep(0.2)

client.loop_forever()    
