# view1.py
import paho.mqtt.client as mqtt
import json
import pygame
from pygame.locals import K_RETURN
pygame.init()

# Set up colors
black = (0, 0, 0)
blue = (0, 0, 255)
yellow = (255, 192, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
grey = (169, 169, 169)
purple = (128, 0, 128)
dark_green = (1, 50, 32)

container_x = 230
container_y = 245

# Set up Rects
Cabin = pygame.Rect(225, 100, 20, 20)
movement_speed = 1
rope_height = 110
container_picked_up = False
leg_bridge = pygame.Rect(330, 200, 115, 10)
Shore_leg1 = pygame.Rect(345, 190, 10, 110)
Shore_leg2 = pygame.Rect(425, 190, 10, 110)
Crane_Leg = pygame.Rect(385, 80, 10, 120)
Bridge = pygame.Rect(225, 90, 200, 10)
Container_1 = pygame.Rect(container_x, container_y, 40, 15)
Waterline = pygame.Rect(75, 300, 250, 50)
shore = pygame.Rect(325, 300, 250, 50)

# set up spreader
spreader_width = 10
spreader_height = 10
spreader_distance = 1

font = pygame.font.Font(None, 20)
text_color = white = (255, 255, 255)

target_container_location = (Container_1.x, Container_1.y)
last_spreader_x = 0
last_spreader_y = 0

# MQTT configurations
mqtt_broker_address = "2939d3617acc492aa3b3653ac474fdc0.s2.eu.hivemq.cloud"
mqtt_port = 8883
mqtt_username = "Admin"
mqtt_password = "hMu4P6L_LAMj8t3"
mqtt_topic_outputs_positionSpreader = "outputs/positionSpreader"
mqtt_topic_outputs_motorHoist = "outputs/motorHoist"
mqtt_topic_outputs_motorCabin = "outputs/motorCabin"


client = mqtt.Client()
client.tls_set(cert_reqs=mqtt.ssl.CERT_NONE)
movement_hoist = ""
movement_cabin = "" 

rope_height = 110

def on_message(client, userdata, message):
    global rope_height,movement_hoist,movement_cabin

    if message.topic == mqtt_topic_outputs_motorHoist:
        print("Message received: " + str(message.payload.decode("utf-8")))
        print("Topic is " + str(message.topic))
        payload_data = json.loads(message.payload.decode('utf-8'))
        movement_hoist = payload_data.get("direction", "")
        speed = payload_data.get("speed", "")

        print(movement_hoist)

        if movement_hoist == "ClockWise":
            print("Performing Clockwise movement at speed:", speed)

        elif movement_hoist == "AntiClockWise":

            print("Performing AntiClockwise movement at speed:", speed)

        elif movement_hoist == "none":
            print("Performing stop", speed)

        else:
            print("Unknown direction:", movement_hoist)

    elif message.topic == mqtt_topic_outputs_motorCabin:
        print("Message received: " + str(message.payload.decode("utf-8")))
        print("Topic is " + str(message.topic))
        payload_data = json.loads(message.payload.decode('utf-8'))
        movement_cabin = payload_data.get("direction", "")
        speed = payload_data.get("speed", "")


        print(movement_cabin)

        if movement_cabin == "clockWise":
            print("Performing Clockwise movement at speed:", speed)

        elif movement_cabin == "antiClockWise":
            print("Performing AntiClockwise movement at speed:", speed)

        elif movement_cabin == "none":
            print("Performing stop")
        else:
            print("Unknown direction:", movement_cabin)

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
    client.subscribe(mqtt_topic_outputs_motorHoist)
    client.subscribe(mqtt_topic_outputs_motorCabin)
except Exception as e:
    print(f"Error connecting to MQTT broker: {e}")



client.loop_start()

def spreader_location(screen, cabin_centerx, cabin_bottom, rope_height, spreader_width, spreader_distance, font, text_color, client, mqtt_topic):
    spreader_x = cabin_centerx - spreader_width // 2
    spreader_y = cabin_bottom + rope_height + spreader_distance
    pygame.draw.rect(screen, yellow, (spreader_x, spreader_y, spreader_width, spreader_height))

    # Show spreader location
    spreader_location_text = font.render(f"Spreader Location: ({spreader_x}, {spreader_y})", True, text_color)
    screen.blit(spreader_location_text, (75, 65))

    spreader_location = {
        "positionX": float(spreader_x),
        "positionY": float(spreader_y)
    }

    client.publish(mqtt_topic, json.dumps(spreader_location))

    return spreader_x, spreader_y

def draw_view1(screen, rope_height, font, text_color):
    global container_picked_up, target_container_location, spreader_x, spreader_y, last_spreader_x, last_spreader_y
    keys = pygame.key.get_pressed()
    # movements hoist
    if movement_hoist == "clockwise" and rope_height > 10:
        rope_height -= movement_speed
    if movement_hoist == "antiClockwise" and rope_height < 180:
        rope_height += movement_speed
    if movement_hoist == "none":
        rope_height = rope_height

    # movments cabin
    if movement_cabin == "clockwise" and Cabin.left > 225:
        Cabin.x -= movement_speed
    if movement_cabin == "antiClockwise" and Cabin.right < 425:
        Cabin.x += movement_speed
    if movement_cabin == "none":
        rope_height = rope_height

    # spreader lock
    if keys[K_RETURN]:
        if not container_picked_up:
            if Container_1.colliderect((spreader_x, spreader_y, spreader_width, spreader_height)):
                container_picked_up = True
        elif container_picked_up:
            container_picked_up = False
            target_container_location = (spreader_x - Container_1.width // 2,
                                         spreader_y + spreader_height + spreader_distance)
            Container_1.topleft = target_container_location

    if container_picked_up:
        Container_1.topleft = (spreader_x - Container_1.width // 2 + 5, spreader_y + spreader_height + spreader_distance)

    # Your drawings (x, y, width, height)
    pygame.draw.rect(screen, yellow, leg_bridge)
    pygame.draw.rect(screen, yellow, Shore_leg1)
    pygame.draw.rect(screen, yellow, Shore_leg2)
    pygame.draw.rect(screen, yellow, Crane_Leg)
    pygame.draw.rect(screen, yellow, Bridge)
    pygame.draw.rect(screen, purple, Cabin)
    pygame.draw.rect(screen, blue, Waterline)

    pygame.draw.rect(screen, grey, shore)

    pygame.draw.line(screen, purple, (Cabin.centerx, Cabin.bottom), (Cabin.centerx, Cabin.bottom + rope_height), 5)  # Rope
    pygame.draw.rect(screen, dark_green, Container_1)

    # spreader_location
    spreader_x, spreader_y = spreader_location(screen, Cabin.centerx, Cabin.bottom, rope_height, spreader_width, spreader_distance, font, text_color, client, mqtt_topic_outputs_positionSpreader)

    # container_location
    container_location_text = font.render(f"Container Location: ({Container_1.x}, {Container_1.y})", True, text_color)
    screen.blit(container_location_text, (75, 85))

    last_spreader_x = spreader_x
    last_spreader_y = spreader_y

    return rope_height