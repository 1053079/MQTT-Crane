# view2.py
from All_views.view1 import *
import pygame
import paho.mqtt.client as mqtt
import json

movement_speed = 1
clock = pygame.time.Clock()

# Colours that we can use for visualisation
white = (255,255,255),
black = (0,0,0),
blue = (0,0,255)
red = (255,0,0)
yellow = (255,192,0)

# Set up Rects

shore_x = 795
shore_y = 200
Waterline_view2 = pygame.Rect(625, 300, 500, 50)
Shore_view2 = pygame.Rect(shore_x, shore_y, 110, 10)
Shore_leg1_view2 = pygame.Rect(shore_x + 10, shore_y - 10, 10, 110)
Shore_leg2_view2 = pygame.Rect(shore_x + 90, shore_y - 10, 10, 110)
Crane_Leg_view2 = pygame.Rect(shore_x + 35, shore_y - 120, 10, 120)

# MQTT configurations
mqtt_broker_address = "2939d3617acc492aa3b3653ac474fdc0.s2.eu.hivemq.cloud"
mqtt_port = 8883
mqtt_username = "Admin"
mqtt_password = "hMu4P6L_LAMj8t3"
mqtt_topic_outputs_motorCrane = "outputs/motorCrane"

client = mqtt.Client()
client.tls_set(cert_reqs=mqtt.ssl.CERT_NONE)
movement_Crane = ""

def on_message(client, userdata, message):
    global movement_Crane
    if message.topic == mqtt_topic_outputs_motorCrane:
        payload_data = json.loads(message.payload.decode('utf-8'))
        movement_Crane = payload_data.get("direction", "")
        print(f"Movement direction: {movement_Crane}")

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
except Exception as e:
    print(f"Error connecting to MQTT broker: {e}")

client.loop_start()

def draw_view2(screen,shore_x, shore_y,resized_boat):
    pygame.draw.rect(screen, yellow, Shore_view2)
    # blits the boat to screen
    screen.blit(resized_boat, (777, 255))
    pygame.draw.rect(screen, blue, Waterline_view2)
    pygame.draw.rect(screen, yellow, Shore_leg1_view2)
    pygame.draw.rect(screen, yellow, Shore_leg2_view2)
    pygame.draw.rect(screen, yellow, Crane_Leg_view2)

    # Move Shore_view2 left and right within limits
    if movement_Crane == "clockwise" and shore_x > 710:
        shore_x -= movement_speed
    if movement_Crane == "antiClockwise" and shore_x < 890:
        shore_x += movement_speed

    Shore_view2.x = shore_x
    Shore_leg1_view2.x = shore_x + 10
    Shore_leg2_view2.x = shore_x + 90
    Crane_Leg_view2.x = shore_x + 50

    clock.tick(30)

    return shore_x, shore_y, resized_boat, Shore_view2, Shore_leg1_view2, Shore_leg2_view2, Crane_Leg_view2, Waterline_view2