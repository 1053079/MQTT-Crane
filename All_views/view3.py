# view3.py
from All_views.view2 import *
import pygame

movement_speed = 1


# Set up colors
black = (0, 0, 0)
blue = (0, 0, 255)
yellow = (255, 192, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
grey = (169, 169, 169)
purple = (128, 0, 128)
dark_green = (1,50,32)

# Movable components and possisions
cabin_x = 225
cabin_y = 545
legs_y = 500
crain_y = 550
legs_bridge1_y = 505
legs_bridge2_y = 595

# MQTT configurations
mqtt_broker_address = "2939d3617acc492aa3b3653ac474fdc0.s2.eu.hivemq.cloud"
mqtt_port = 8883
mqtt_username = "Admin"
mqtt_password = "hMu4P6L_LAMj8t3"
mqtt_topic_outputs_motorCrane = "outputs/motorCrane"

client = mqtt.Client()
client.tls_set(cert_reqs=mqtt.ssl.CERT_NONE)
movement_Crane = ""
movement_cabin = ""

def on_message(client, userdata, message):
    global movement_Crane,movement_cabin
    if message.topic == mqtt_topic_outputs_motorCrane:
        payload_data = json.loads(message.payload.decode('utf-8'))
        movement_Crane = payload_data.get("direction", "")
        print(f"Movement direction: {movement_Crane}")
    elif message.topic == mqtt_topic_outputs_motorCabin:
        payload_data = json.loads(message.payload.decode('utf-8'))
        movement_cabin = payload_data.get("direction", "")
        speed = payload_data.get("speed", "")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print(f"Failed to connect, return code: {rc}")

def on_disconnect(client, userdata, rc):
    if rc == 0:
        print("Disconnected from MQTT broker")
    else:
        print(f"Unexpected disconnection, return code: {rc}")


client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.username_pw_set(mqtt_username, mqtt_password)
client.on_message = on_message

try:
    client.connect(mqtt_broker_address, mqtt_port, 60)
    client.subscribe(mqtt_topic_outputs_motorCrane)
    client.subscribe(mqtt_topic_outputs_motorCabin)
except Exception as e:
    print(f"Error connecting to MQTT broker: {e}")

client.loop_start()



def draw_view3(screen, cabin_x, cabin_y, legs_y, crain_y, legs_bridge1_y, legs_bridge2_y):
    # Movement view 3
    keys = pygame.key.get_pressed()

    # Handle movement for the cabin
    if movement_Crane == "clockwise":
        cabin_y -= movement_speed
    if movement_Crane == "antiClockwise":
        cabin_y += movement_speed
    if movement_cabin == "clockwise":
        cabin_x -= movement_speed
    if movement_cabin == "anitClockwise":
        cabin_x += movement_speed
    if movement_cabin == "none":
        cabin_y = cabin_y
    cabin_x = max(225, min(cabin_x, 405))
    cabin_y = max(445, min(cabin_y, 635))

    # Handle movement for the legs
    if movement_Crane == "clockwise":
        legs_y -= movement_speed
    if movement_Crane == "antiClockwise":
        legs_y += movement_speed
    legs_y = max(400, min(legs_y, 590))

    # Handle movement for the crane
    if movement_Crane == "clockwise":
        crain_y -= movement_speed
    if movement_Crane == "antiClockwise":
        crain_y += movement_speed
    crain_y = max(450, min(crain_y, 640))

    # Handle movement for the crane
    if movement_Crane == "clockwise":
        legs_bridge1_y -= movement_speed
    if movement_Crane == "antiClockwise":
        legs_bridge1_y += movement_speed
    legs_bridge1_y = max(405, min(legs_bridge1_y, 595))

    # Handle movement for the crane
    if movement_Crane == "clockwise":
        legs_bridge2_y -= movement_speed
    if movement_Crane == "antiClockwise":
        legs_bridge2_y += movement_speed
    legs_bridge2_y = max(495, min(legs_bridge2_y, 685))

    # Draw View 3
    pygame.draw.rect(screen, grey, (325, 400, 250, 300))  # Shore
    pygame.draw.rect(screen, blue, (75, 400, 250, 300))  # Water

    pygame.draw.rect(screen, red, (200, 500, 100, 150))  # boat
    pygame.draw.circle(screen, red, [250, 500], 50, 0)  # boat

    #pygame.draw.rect(screen, dark_green, (230, 525, 40, 75))  # container

    #pygame.draw.rect(screen, purple, (cabin_x, cabin_y, 20, 20))  # cabin
    pygame.draw.rect(screen, yellow, (225, crain_y, 200, 10))  # crain

    pygame.draw.rect(screen, yellow, (345, legs_y, 10, 110))  # legs
    pygame.draw.rect(screen, yellow, (425, legs_y, 10, 110))  # legs

    pygame.draw.rect(screen, yellow, (330, legs_bridge1_y, 115, 10))  # legs_bridge
    pygame.draw.rect(screen, yellow, (330, legs_bridge2_y, 115, 10))  # legs_bridge

    return cabin_x, cabin_y, legs_y, crain_y, legs_bridge1_y, legs_bridge2_y