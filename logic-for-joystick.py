import paho.mqtt.client as mqtt
import keyboard
import json

address = "2939d3617acc492aa3b3653ac474fdc0.s2.eu.hivemq.cloud"
port = 8883

topic_1 = "keyboard/inputs"

client = mqtt.Client()

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected to broker")
    else:
        print(f"Connection failed with code {rc}")

client.on_connect = on_connect


# TLS (required for connection)
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# Username and password (required for connection)
client.username_pw_set("Admin", "hMu4P6L_LAMj8t3")


# Default values
movement = "none"
speed = "normal"
lock = False

# Main Loop
try:
    client.connect(address, port)
    client.loop_start()
    while True:
        key_event = keyboard.read_event()

        # Movement
        if key_event.name == "w": movement = "w", print("W key sent")
        elif key_event.name == "a": movement = "a", print("A key sent")
        elif key_event.name == "s": movement = "s", print("S key sent")
        elif key_event.name == "d": movement = "d", print("D key sent")
        elif key_event.name == "up": movement = "up-arrow", print("Up-Arrow key sent")
        elif key_event.name == "left": movement = "left-arrow", print("Left-Arrow key sent")
        elif key_event.name == "down": movement = "down-arrow", print("Down-Arrow key sent")
        elif key_event.name == "right": movement = "right-arrow", print("Right-Arrow key sent")
        else:
            movement = None

        # Speed of movement
        if key_event.name == "left shift": speed = "fast"
        elif key_event.name == "left ctrl": speed = "slow"
        elif key_event.event_type == keyboard.KEY_UP and (key_event.name == "left shift" or key_event.name == "left ctrl"): speed = "normal"

        # Lock/unlock spreader
        elif key_event.name == "enter" and key_event.event_type == keyboard.KEY_DOWN:
            lock = not lock

        # Payload
        payload = {"movement": movement, "speed": speed, "lock": lock}

        payload_string = json.dumps(payload)

        client.publish(topic_1, payload_string, qos=0)

except KeyboardInterrupt:
    print("Disconnecting: Keyboard Interrupt")
    client.loop_stop()
    client.disconnect()