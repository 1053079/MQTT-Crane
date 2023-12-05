import paho.mqtt.client as mqttclient
import time

def on_connect(client,userdata,flags,rc):
    if rc==0:
        print("client is connected")
        global connected
        connected = True
    else:
        print("client is not connected")

def on_message(client, userdata,message):
    print("Message received " + str(message.payload.decode("utf-8")))
    print("Topic " + str(message.topic))

connected= False
messageReceived= False

broker = "2939d3617acc492aa3b3653ac474fdc0.s2.eu.hivemq.cloud"
port = 8883
username = "Admin"
password = "hMu4P6L_LAMj8t3"

client = mqttclient.Client("MQTT")
client.username_pw_set(username, password)
client.on_connect = on_connect
client.connect(broker, port)
client.loop_start()
client.subscribe("keyboard/inputs")

while connected!= True:
    time.sleep(0.2)
while messageReceived!= True: 
    time.sleep(0.2)

client.loop_stop()    
