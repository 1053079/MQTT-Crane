import pygame
import paho.mqtt.client as mqtt
import json



pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Dit zijn de variabelen voor de images
arrow_up = pygame.image.load('images/arrow_up.png').convert_alpha()
arrow_down = pygame.image.load('images/arrow_down.png').convert_alpha()
arrow_left = pygame.image.load('images/arrow_left.png').convert_alpha()
arrow_right = pygame.image.load('images/arrow_right.png').convert_alpha()
arrow_upstairs = pygame.image.load('images/arrow_upstairs.png').convert_alpha()
arrow_downstairs = pygame.image.load('images/arrow_downstairs.png').convert_alpha()
locked = pygame.image.load('images/locked.png').convert_alpha()
unlocked = pygame.image.load('images/unlocked.png').convert_alpha()
siren = pygame.image.load('images/siren.png').convert_alpha()
emergency = pygame.image.load('images/emergency.png').convert_alpha()
forwardLeft = pygame.image.load('images/forwardLeft.png').convert_alpha()
forwardRight = pygame.image.load('images/forwardRight.png').convert_alpha()
backwardLeft = pygame.image.load('images/backwardLeft.png').convert_alpha()
backwardRight = pygame.image.load('images/backwardRight.png').convert_alpha()

# dit definieert de  breedte en hoogte van de PNG
new_arrow_width = 100
new_arrow_height = 100

# Dit wijzigt de grootte van de PNG's
arrow_up = pygame.transform.scale(arrow_up, (new_arrow_width, new_arrow_height))
arrow_down = pygame.transform.scale(arrow_down, (new_arrow_width, new_arrow_height))
arrow_left = pygame.transform.scale(arrow_left, (new_arrow_width, new_arrow_height))
arrow_right = pygame.transform.scale(arrow_right, (new_arrow_width, new_arrow_height))
arrow_upstairs = pygame.transform.scale(arrow_upstairs, (new_arrow_width, new_arrow_height))
arrow_downstairs = pygame.transform.scale(arrow_downstairs, (new_arrow_width, new_arrow_height))
locked = pygame.transform.scale(locked, (new_arrow_width, new_arrow_height))
unlocked = pygame.transform.scale(unlocked, (new_arrow_width, new_arrow_height))
siren = pygame.transform.scale(siren, (new_arrow_width, new_arrow_height))
emergency = pygame.transform.scale(emergency, (new_arrow_width, new_arrow_height))
forwardLeft = pygame.transform.scale(forwardLeft, (new_arrow_width, new_arrow_height))
forwardRight = pygame.transform.scale(forwardRight, (new_arrow_width, new_arrow_height))
backwardLeft = pygame.transform.scale(backwardLeft, (new_arrow_width, new_arrow_height))
backwardRight = pygame.transform.scale(backwardRight, (new_arrow_width, new_arrow_height))

# Werkt de breedte en hoogte variabelen bij
arrow_width = new_arrow_width
arrow_height = new_arrow_height

# Positie van de images
arrow_up_rect = arrow_up.get_rect(topleft=(SCREEN_WIDTH // 2 - arrow_width // 2, SCREEN_HEIGHT - arrow_height * 2))
arrow_down_rect = arrow_down.get_rect(topleft=(SCREEN_WIDTH // 2 - arrow_width // 2, SCREEN_HEIGHT - arrow_height))
arrow_left_rect = arrow_left.get_rect(topleft=(SCREEN_WIDTH // 2 - arrow_width * 2.1, SCREEN_HEIGHT - arrow_height * 1.5))
arrow_right_rect = arrow_right.get_rect(topleft=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - arrow_height * 1.5))


arrow_upstairs_rect = arrow_upstairs.get_rect(topleft=(SCREEN_WIDTH // 2 + 20, SCREEN_HEIGHT - arrow_height * 3))
arrow_downstairs_rect = arrow_downstairs.get_rect(topleft=(SCREEN_WIDTH // 2 + 20, SCREEN_HEIGHT - arrow_height))

locked_rect = locked.get_rect(topleft=(SCREEN_WIDTH // 2 + 470, SCREEN_HEIGHT - arrow_height * 3))
unlocked_rect = unlocked.get_rect(topleft=(SCREEN_WIDTH // 2 + 470, SCREEN_HEIGHT - arrow_height * 2))

siren_rect = siren.get_rect(topleft=(SCREEN_WIDTH // 2 + 470, SCREEN_HEIGHT - arrow_height))
emergency_rect = emergency.get_rect(topleft=(SCREEN_WIDTH // 2 + 470, SCREEN_HEIGHT - arrow_height * 4))


forwardLeft_rect = forwardLeft.get_rect(topleft=(SCREEN_WIDTH // 2 - arrow_width // 2, SCREEN_HEIGHT - arrow_height * 2))
forwardRight_rect = forwardRight.get_rect(topleft=(SCREEN_WIDTH // 2 - arrow_width // 2, SCREEN_HEIGHT - arrow_height))
backwardLeft_rect = backwardLeft.get_rect(topleft=(SCREEN_WIDTH // 2 - arrow_width * 2.1, SCREEN_HEIGHT - arrow_height * 1.5))
backwardRight_rect = backwardRight.get_rect(topleft=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - arrow_height * 1.5))

# Dit voegt de MQTT-gegevens toe:
mqtt_username = "Admin"
mqtt_password = "hMu4P6L_LAMj8t3"
mqtt_broker_address = "2939d3617acc492aa3b3653ac474fdc0.s2.eu.hivemq.cloud"
mqtt_port = 8883
mqtt_topic = "inputs/joystick"

movement = "none"
speed = "normal"
lock = False

# Dit voegt de MQTT-client en -callbacks toe:
client = mqtt.Client()


def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected to broker")
    else:
        print(f"Connection failed with code {rc}")

def on_message(client, userdata, message):

    global movement, speed, lock  

    print(message.topic)
    payload = json.loads(message.payload.decode("utf-8"))
    print(payload)

    
    movement = payload.get("movement", "none")
    speed = payload.get("speed", "normal")
    lock = payload.get("lock", False)

    
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(cert_reqs=mqtt.ssl.CERT_NONE)
client.username_pw_set(mqtt_username, mqtt_password)

# Dit verbind met de MQTT-server en abonneert op het juiste onderwerp:
client.connect(mqtt_broker_address, mqtt_port)
client.subscribe(mqtt_topic)

run = True
while run:
    # Dit luister naar MQTT-berichten
    client.loop()

    keys = pygame.key.get_pressed()

    # dit zorgt voor een grijze achtergrond
    screen.fill((128, 128, 128))

    # Dit update de positie van de PNG's (pas deze aan naar wens)
    arrow_up_rect.topleft = (SCREEN_WIDTH // 2 + 320 - arrow_width // 2, SCREEN_HEIGHT - arrow_height * 2)
    arrow_down_rect.topleft = (SCREEN_WIDTH // 2 + 320 - arrow_width // 2, SCREEN_HEIGHT - arrow_height)
    arrow_left_rect.topleft = (SCREEN_WIDTH // 2 + 430 - arrow_width * 2.1, SCREEN_HEIGHT - arrow_height * 1.5)
    arrow_right_rect.topleft = (SCREEN_WIDTH // 2 + 320 , SCREEN_HEIGHT - arrow_height * 1.5)

    arrow_upstairs_rect.topleft = (SCREEN_WIDTH // 2 + 450, SCREEN_HEIGHT - arrow_height * 3)
    arrow_downstairs_rect.topleft = (SCREEN_WIDTH // 2 + 450, SCREEN_HEIGHT - arrow_height)

    forwardLeft_rect.topleft = (SCREEN_WIDTH // 2 - arrow_width + 300, SCREEN_HEIGHT - arrow_height * 2.5)
    forwardRight_rect.topleft = (SCREEN_WIDTH // 2 - arrow_width + 450, SCREEN_HEIGHT - arrow_height * 2.5)
    backwardLeft_rect.topleft = (SCREEN_WIDTH // 2 - arrow_width + 300, SCREEN_HEIGHT - arrow_height * 1.5)
    backwardRight_rect.topleft = (SCREEN_WIDTH // 2 - arrow_width + 450, SCREEN_HEIGHT - arrow_height * 1.5)

    # Dit zorgt ervoor dat de images verschijnen als de toetsen worden ingedrukt
    if movement == 'forward':
        screen.blit(arrow_up, arrow_up_rect)

    if movement == 'backward':
        screen.blit(arrow_down, arrow_down_rect)

    if movement == 'left':
        screen.blit(arrow_left, arrow_left_rect)

    if movement == 'right':
        screen.blit(arrow_right, arrow_right_rect)

    if movement == 'up':
        screen.blit(arrow_upstairs, arrow_upstairs_rect)
            
    if movement == 'down':
        screen.blit(arrow_downstairs, arrow_downstairs_rect)

    if lock:
        screen.blit(locked, locked_rect)
    else:
        screen.blit(unlocked, unlocked_rect)

    if movement == 'forwardLeft' :
        screen.blit(forwardLeft, forwardLeft_rect)
    if movement == 'forwardRight' :
        screen.blit(forwardRight, forwardRight_rect)
    if movement == 'backwardLeft' :
        screen.blit(backwardLeft, backwardLeft_rect)
    if movement == 'backwardRight' :
        screen.blit(backwardRight, backwardRight_rect)

  
    pygame.display.flip()

pygame.quit()