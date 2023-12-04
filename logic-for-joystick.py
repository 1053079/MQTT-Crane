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

        while True:
            try:
                if keyboard.is_pressed('w'):
                    print('W key is pressed')
                    movement = 'w'
                    break
                if keyboard.is_pressed('a'):
                    print('A key is pressed')
                    movement = 'a'
                    break
                if keyboard.is_pressed('s'):
                    print('S key is pressed')
                    movement = 's'
                    break
                if keyboard.is_pressed('d'):
                    print('D key is pressed')
                    movement = 'd'
                    break
                if keyboard.is_pressed('up'):
                    print('Up Arrow key is pressed')
                    movement = 'up'
                    break
                if keyboard.is_pressed('down'):
                    print('Down Arrow key is pressed')
                    movement = 'down'
                    break
                if keyboard.is_pressed('enter'):
                    print('Enter key is pressed')
                    lock = not lock
                    movement = 'none'
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
        payload = {"movement": movement, "speed": speed, "lock": lock}
        payload_string = json.dumps(payload)
        client.publish(topic_1, payload_string, qos=0)
        print(payload)

except KeyboardInterrupt:
    print("Disconnecting: Keyboard Interrupt")
    client.loop_stop()
    client.disconnect()