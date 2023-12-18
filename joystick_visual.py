
import paho.mqtt.client as mqtt
import json


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

def visuals():
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


# Dit voegt de MQTT-client en -callbacks toe:

