import pygame
import paho.mqtt.client as mqtt
import json


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Dit zijn de variabelen voor de images
arrow_up = 'images/arrow_up.png'
arrow_down ='images/arrow_down.png'
arrow_left = 'images/arrow_left.png'
arrow_right = 'images/arrow_right.png'
arrow_upstairs = 'images/arrow_upstairs.png'
arrow_downstairs = 'images/arrow_downstairs.png'
locked ='images/locked.png'
unlocked ='images/unlocked.png'
siren = 'images/siren.png'
emergencyButton = 'images/emergency.png'
forwardLeft = 'images/forwardLeft.png'
forwardRight = 'images/forwardRight.png'
backwardLeft = 'images/backwardLeft.png'
backwardRight = 'images/backwardRight.png'

# # dit definieert de  breedte en hoogte van de PNG
# new_arrow_width = 100
# new_arrow_height = 100

# # Dit wijzigt de grootte van de PNG's
# arrow_up = pygame.transform.scale(arrow_up, (new_arrow_width, new_arrow_height))
# arrow_down = pygame.transform.scale(arrow_down, (new_arrow_width, new_arrow_height))
# arrow_left = pygame.transform.scale(arrow_left, (new_arrow_width, new_arrow_height))
# arrow_right = pygame.transform.scale(arrow_right, (new_arrow_width, new_arrow_height))
# arrow_upstairs = pygame.transform.scale(arrow_upstairs, (new_arrow_width, new_arrow_height))
# arrow_downstairs = pygame.transform.scale(arrow_downstairs, (new_arrow_width, new_arrow_height))
# locked = pygame.transform.scale(locked, (new_arrow_width, new_arrow_height))
# unlocked = pygame.transform.scale(unlocked, (new_arrow_width, new_arrow_height))
# siren = pygame.transform.scale(siren, (new_arrow_width, new_arrow_height))
# emergency = pygame.transform.scale(emergency, (new_arrow_width, new_arrow_height))
# forwardLeft = pygame.transform.scale(forwardLeft, (new_arrow_width, new_arrow_height))
# forwardRight = pygame.transform.scale(forwardRight, (new_arrow_width, new_arrow_height))
# backwardLeft = pygame.transform.scale(backwardLeft, (new_arrow_width, new_arrow_height))
# backwardRight = pygame.transform.scale(backwardRight, (new_arrow_width, new_arrow_height))

# # Werkt de breedte en hoogte variabelen bij
# arrow_width = new_arrow_width
# arrow_height = new_arrow_height

# # Positie van de images
# arrow_up_rect = arrow_up.get_rect(topleft=(SCREEN_WIDTH // 2 - arrow_width // 2, SCREEN_HEIGHT - arrow_height * 2))
# arrow_down_rect = arrow_down.get_rect(topleft=(SCREEN_WIDTH // 2 - arrow_width // 2, SCREEN_HEIGHT - arrow_height))
# arrow_left_rect = arrow_left.get_rect(topleft=(SCREEN_WIDTH // 2 - arrow_width * 2.1, SCREEN_HEIGHT - arrow_height * 1.5))
# arrow_right_rect = arrow_right.get_rect(topleft=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - arrow_height * 1.5))


# arrow_upstairs_rect = arrow_upstairs.get_rect(topleft=(SCREEN_WIDTH // 2 + 20, SCREEN_HEIGHT - arrow_height * 3))
# arrow_downstairs_rect = arrow_downstairs.get_rect(topleft=(SCREEN_WIDTH // 2 + 20, SCREEN_HEIGHT - arrow_height))

# locked_rect = locked.get_rect(topleft=(SCREEN_WIDTH // 2 + 470, SCREEN_HEIGHT - arrow_height * 3))
# unlocked_rect = unlocked.get_rect(topleft=(SCREEN_WIDTH // 2 + 470, SCREEN_HEIGHT - arrow_height * 2))

# siren_rect = siren.get_rect(topleft=(SCREEN_WIDTH // 2 + 470, SCREEN_HEIGHT - arrow_height))
# emergency_rect = emergency.get_rect(topleft=(SCREEN_WIDTH // 2 + 470, SCREEN_HEIGHT - arrow_height * 4))


# forwardLeft_rect = forwardLeft.get_rect(topleft=(SCREEN_WIDTH // 2 - arrow_width // 2, SCREEN_HEIGHT - arrow_height * 2))
# forwardRight_rect = forwardRight.get_rect(topleft=(SCREEN_WIDTH // 2 - arrow_width // 2, SCREEN_HEIGHT - arrow_height))
# backwardLeft_rect = backwardLeft.get_rect(topleft=(SCREEN_WIDTH // 2 - arrow_width * 2.1, SCREEN_HEIGHT - arrow_height * 1.5))
# backwardRight_rect = backwardRight.get_rect(topleft=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - arrow_height * 1.5))

# Dit voegt de MQTT-gegevens toe:
mqtt_username = "Admin"
mqtt_password = "hMu4P6L_LAMj8t3"
mqtt_broker_address = "2939d3617acc492aa3b3653ac474fdc0.s2.eu.hivemq.cloud"
mqtt_port = 8883
mqtt_topic = "inputs/joystick"
mqtt_topic2 = "inputs/cabinEmergencyButton"

# topic we send output to
topic_1 = "outputs/joyStickVisuals"

# Dit voegt de MQTT-client en -callbacks toe:
client = mqtt.Client()

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected to broker")
    else:
        print(f"Connection failed with code {rc}")

def on_message(client, userdata, message):
    print(message.topic)
    payload = json.loads(message.payload.decode("utf-8"))
    print(payload)
    if message.topic == mqtt_topic2: # checks for topic
        print("Message received: " + str((message.payload.decode("utf-8"))))
        print("Topic is " + str(message.topic))
    else: 
        print("Message received is " + str((message.payload.decode("utf-8"))))
        print("Topic is " + str(message.topic)) 
    # decodes the JSON and allows us to get the values of the movement, speed and lock.
    payload_data = json.loads(message.payload.decode('utf-8'))
    movement = payload_data.get("movement") # The movement of the joystick input
    speed = payload_data.get("speed") # Speed from joystick input, we will adjust this in our payload
    lock = payload_data.get("lock") # Checks whether spreader is locked or not
    emergency = payload_data.get("emergency") # Checks for emergency from the inputs/cabinEmergencyButton

    try:
        if emergency is False:
            positionXY = (1025,350)
            image = unlocked
            print("lock is false") 
            
            if movement == 'forward':
                positionXY = (690,515)
                image = arrow_up
                print(positionXY , image)
            elif movement == 'backward':
                positionXY = (690,590)
                image = arrow_down
                print(positionXY , image)
            elif movement == 'left':
                positionXY = (653,555)
                image = arrow_left
                print(positionXY , image)
            elif movement == 'right':
                positionXY = (730,555)
                image = arrow_right
                print(positionXY , image)
            elif movement == 'up':
                positionXY = (847, 450)
                image = arrow_upstairs
                print(positionXY , image)
            elif movement == 'down':
                positionXY = (847, 630)
                image = arrow_downstairs
                print(positionXY , image)
            elif movement == 'forwardLeft' :
                positionXY = (640 , 500)
                image = forwardLeft
                print(positionXY , image)
            elif movement == 'forwardRight' :
                positionXY = (740 , 500)
                image = forwardRight
                print(positionXY , image)
            elif movement == 'backwardLeft' :
                positionXY = (640, 600)
                image = backwardLeft
                print(positionXY , image)
            elif movement == 'backwardRight' :
                positionXY = (740, 600)
                image = backwardRight
                print(positionXY , image)
            else:
                print("Invalid key has been detected " + movement)
        else:
            positionXY = (1025,360)
            image = locked
            print("lock is true")
    except Exception as e:
        print(e)
    # Payload that we send to outputs/joyStickVisuals, which is output/motorCabin
    position = list(positionXY)
    payload = {"movement": movement, "position": position, "image": image, "lock": lock, "emergency": emergency}
    payload_string = json.dumps(payload)
    client.publish(topic_1, payload_string, qos=0)

    
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(cert_reqs=mqtt.ssl.CERT_NONE)
client.username_pw_set(mqtt_username, mqtt_password)

# Dit verbind met de MQTT-server en abonneert op het juiste onderwerp:
client.connect(mqtt_broker_address, mqtt_port)
client.subscribe([(mqtt_topic, 0) , (mqtt_topic2, 0)])
client.loop_forever()

