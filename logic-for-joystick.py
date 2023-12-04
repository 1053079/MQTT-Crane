import paho.mqtt.client as mqtt
import keyboard
import json
import pyautogui

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
        if key_event.name == "w" and key_event.event_type == keyboard.KEY_DOWN:
            movement = "w"
            print("W key sent")
        elif key_event.name == "a" and key_event.event_type == keyboard.KEY_DOWN:
            movement = "a"
            print("A key sent")
        elif key_event.name == "s" and key_event.event_type == keyboard.KEY_DOWN:
            movement = "s"
            print("S key sent")
        elif key_event.name == "d" and key_event.event_type == keyboard.KEY_DOWN:
            movement = "d"
            print("D key sent")
        elif key_event.name == "up" and key_event.event_type == keyboard.KEY_DOWN:
            movement = "up-arrow"
            print("Up-Arrow key sent")
        elif key_event.name == "left" and key_event.event_type == keyboard.KEY_DOWN:
            movement = "left-arrow"
            print("Left-Arrow key sent")
        elif key_event.name == "down" and key_event.event_type == keyboard.KEY_DOWN:
            movement = "down-arrow"
            print("Down-Arrow key sent")
        elif key_event.name == "right" and key_event.event_type == keyboard.KEY_DOWN:
            movement = "right-arrow"
            print("Right-Arrow key sent")
        else:
            movement = "none"

        # Speed of movement
        shift_pressed = keyboard.is_pressed('shift')
        ctrl_pressed = keyboard.is_pressed('ctrl')

        if shift_pressed:
            speed = "fast"
        elif ctrl_pressed:
            speed = "slow"
        else:
            speed = "normal"

        # Lock/unlock spreader
        if key_event.name == "enter" and key_event.event_type == keyboard.KEY_DOWN:
            lock = not lock

        # Payload
        payload = {"movement": movement, "speed": speed, "lock": lock}

        payload_string = json.dumps(payload)

        client.publish(topic_1, payload_string, qos=0)

except KeyboardInterrupt:
    print("Disconnecting: Keyboard Interrupt")
    client.loop_stop()
    client.disconnect()