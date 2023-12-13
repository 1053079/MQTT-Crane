import paho.mqtt.client as mqtt
import time
import json

# topics that we are subscribed to
topic_1 = "outputs/motorHoist"

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

    print (payload_data)
    try:  
      if payload_data: 
       if movement == "up" or "down": 
        if speed == "normal" : ## normal speed
          # Up and down are for the Hoist movements
         if movement == "up":
             print("You have pressed " + movement + " at normal hoistspeed ")
         elif movement == "down":    
             print("You have pressed " + movement + " at normal hoistspeed ")
         else:
             print("Invalid key detected")      

        # for fast speed
        elif speed == "fast":
          # Up and down are for the Hoist movements
         if movement == "up":
              print("You have pressed " + movement + " at fast hoistspeed")
         elif movement == "down":    
              print("You have pressed " + movement + " at fast hoistspeed")   
         else:
              print("invalid key detected")  

        # for slow speed      
        elif speed == "slow":       
          # Up and down are for the Hoist movements
         if movement == "up":
              print("You have pressed " + movement + " at slow hoistspeed") 
         elif movement == "down":    
              print("You have pressed " + movement + " at slow hoistspeed")   
         else:
              print("Invalid key detected")         
      else:
              print("Invalid key has been detected")       
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
client.subscribe(topic_1) # Subscribed to the topic
client.loop_start()

while connected!= True:
    time.sleep(0.2)
while messageReceived!= True: 
    time.sleep(0.2)

client.loop_forever()    
