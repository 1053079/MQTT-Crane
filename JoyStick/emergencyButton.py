import paho.mqtt.client as mqtt
import keyboard
import json

address = "2939d3617acc492aa3b3653ac474fdc0.s2.eu.hivemq.cloud" # Pull Request comment 1: Address van broker. Dit is belangrijk, want anders kan je niet connecten.
port = 8883 # Pull Request comment 1: Port van broker. Dit hoort bij de address. Ook belangrijk voor connectie.

# Pull Request comment 1: MQTT topic naam om naar te publishen, en subscribers kunnen subscriben op deze topic om de data te ontvangen
topic_1 = "inputs/cabinEmergencybutton"

# Pull Request comment 1: MQTT client aanmaken (in een variable gezet) om later mee te connecten
client = mqtt.Client()

# Pull Request comment 1: Callback functie voor als de client verbonden is met de broker. De RC parameter (Return Code) geeft aan of de connectie succesvol is of niet.
# Pull Request comment 1: properties=None is een extra parameter die we niet gebruiken, maar wel moeten meegeven, anders maaktie geen connectie (ik had gisteren hier uren aan verspild).
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected to broker")
    else:
        print(f"Connection failed with code {rc}")

client.on_connect = on_connect


# Pull Request comment 1: TLS (required for connection) - Dit was ook blijkbaar nodig voor de connectie, ook uren aan verspild. TLS zorgt voor een beveiligde connectie.
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# Username and password (required for connection)
client.username_pw_set("Admin", "hMu4P6L_LAMj8t3")


# Default values
movement = "none"
speed = "normal"
lock = False
emergency = False

# Main Loop
try:
    client.connect(address, port)
    client.loop_start()
    while True:
        key_event = keyboard.read_event()

        while True:
            try:
                if keyboard.is_pressed('1'):
                    print('Dock Emergency key is pressed')
                    movement = 'dockEmergency'
                    break
                if keyboard.is_pressed('2'):
                    print('Cabin Emergency key is pressed')
                    emergency = not emergency
                    movement = 'cabinEmergency'
                    break
            except:
                break

        # Speed of movement
        shift_pressed = keyboard.is_pressed('shift')
        ctrl_pressed = keyboard.is_pressed('ctrl')

        if shift_pressed:
            speed = "fast"
        elif ctrl_pressed:
            speed = "slow"
        else:
            speed = "normal"

        # Payload
        payload = {"emergency": emergency}
        payload_string = json.dumps(payload)
        client.publish(topic_1, payload_string, qos=0)
        print(payload)

except KeyboardInterrupt:
    print("Disconnecting: Keyboard Interrupt")
    client.loop_stop()
    client.disconnect()