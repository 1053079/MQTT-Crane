
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
    
    payload_data= json.loads(message.payload.decode('utf-8'))
    movement = payload_data.get("movement")

    try:
        if movement == "w":
             print("You have pressed " + movement)
        elif movement =="a":
             print("You have pressed " + movement)
        elif movement== "s":
             print("You have pressed " + movement)
        elif movement== "d":   
             print("You have pressed " + movement)   
        else:
         print("There was an error trying to get " + movement)
    except:
        print("There was an error trying to get " + movement)



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
client.loop_start()
client.subscribe("keyboard/inputs")

while connected!= True:
    time.sleep(0.2)
while messageReceived!= True: 
    time.sleep(0.2)

client.loop_forever()    
