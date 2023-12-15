import pygame 
import os  
import paho.mqtt.client as mqtt
import time
import json

# connects us to the MQTT client
client = mqtt.Client()

# topics that we are subscribed to
topic = "inputs/joyStickVisuals"
topic_1 = "inputs/cabinEmergencyButton"

movement = 'none'
lock = False
position = 0
image = 'image/locked.png'
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected to broker")
    else:
        print(f"Connection failed with code {rc}")

# prints back the message received and the topic
def on_message(client, userdata,message):
    global movement, speed, lock, emergency, position, image, imageName
    if message.topic == topic_1: # checks for topic
     print("Message received: " + str((message.payload.decode("utf-8"))))
     print("Topic is " + str(message.topic))
    else: 
     print("Message received is " + str((message.payload.decode("utf-8"))))
     print("Topic is " + str(message.topic))

    # decodes the JSON and allows us to get the values of the movement, speed and lock.
    payload_data = json.loads(message.payload.decode('utf-8'))
    movement = payload_data.get("movement") # The movement of the joystick input
    speed = payload_data.get("speed")
    lock = payload_data.get("lock") # Checks whether spreader is locked or not
    emergency = payload_data.get("emergency")
    positionList = payload_data.get("position") 
    position = tuple(positionList)
    image = payload_data.get("image")
    split = image.split("/")
    imageName = split[-1]

    print(payload_data)
    print(position)
    print(imageName)

    

# Dit voegt de MQTT-gegevens toe:
mqtt_username = "Admin"
mqtt_password = "hMu4P6L_LAMj8t3"
mqtt_broker_address = "2939d3617acc492aa3b3653ac474fdc0.s2.eu.hivemq.cloud"
mqtt_port = 8883
mqtt_topic = "outputs/joyStickVisuals"

client.on_connect = on_connect
client.on_message = on_message

client.tls_set(cert_reqs=mqtt.ssl.CERT_NONE)
client.username_pw_set(mqtt_username, mqtt_password)

# Dit verbind met de MQTT-server en abonneert op het juiste onderwerp:
client.connect(mqtt_broker_address, mqtt_port)
client.subscribe(mqtt_topic)
client.loop()
# Initialize pygame
pygame.init() 


# Creates the screen allows you to change the (Width, Height) in px.
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 

# This is the title of the screen you see above the screen.
pygame.display.set_caption("Elephant Crane") 
exit = False
# Colours that we can use for visualisation
white = (255,255,255),
black = (0,0,0),
blue = (0,0,255)
skyBlue = (0,255,255)
blueDeFrance = (49,140,231)

# The screens.. parameters are [Width, Height]
view = pygame.Surface([500,300])
view2 = pygame.Surface([500,300])
view3 = pygame.Surface([500,300])

# Controls
# Dit zijn de variabelen voor de images
# arrow_up = pygame.image.load('images/arrow_up.png').convert_alpha()
# arrow_down = pygame.image.load('images/arrow_down.png').convert_alpha()
# arrow_left = pygame.image.load('images/arrow_left.png').convert_alpha()
# arrow_right = pygame.image.load('images/arrow_right.png').convert_alpha()
# arrow_upstairs = pygame.image.load('images/arrow_upstairs.png').convert_alpha()
# arrow_downstairs = pygame.image.load('images/arrow_downstairs.png').convert_alpha()
locked = pygame.image.load('images/locked.png').convert_alpha()
unlocked = pygame.image.load('images/unlocked.png').convert_alpha()
siren = pygame.image.load('images/siren.png').convert_alpha()
# emergency = pygame.image.load('images/emergency.png').convert_alpha()
# forwardLeft = pygame.image.load('images/forwardLeft.png').convert_alpha()
# forwardRight = pygame.image.load('images/forwardRight.png').convert_alpha()
# backwardLeft = pygame.image.load('images/backwardLeft.png').convert_alpha()
# backwardRight = pygame.image.load('images/backwardRight.png').convert_alpha()
emergencyButton = pygame.image.load('images/emergency.png').convert_alpha()
# WASD arrows
WASD = pygame.image.load('UserInterface/buttons/wasdKeys.png')

# Arrow in middle
arrow = pygame.image.load('UserInterface/buttons/arrowKey.png')

# circle buttons
circle = pygame.image.load('UserInterface/buttons/xButton.png')
# circle = pygame.Surface((60,60), pygame.SRCALPHA)
# drawCircle = pygame.draw.circle(circle, white, (30,30), 30)
# xLines = pygame.draw.line(circle, black,(5,5),(55,55), 2)
# xLines2 = pygame.draw.line(circle, black, (30 + 30, 30 - 30), (30 - 30, 30 + 30), 2)

circle2 = pygame.image.load('UserInterface/buttons/plusButton.png')
# circle2 = pygame.Surface((60,60), pygame.SRCALPHA)
# drawCircle2 = pygame.draw.circle(circle2, white, (30,30), 30)

# the while loop..
while not exit: 
    client.loop()
    # Fills the background with blue color
    screen.fill(blueDeFrance)

    # blits the views to the screen. the parameters are the x and y coordinates.
    screen.blit(view, (75,50)) 
    screen.blit(view2, (625,50))
    screen.blit(view3, (75,400))
   
    
    
    # Blits WASD Keys
    screen.blit(WASD, (650, 500))
    # BLits the arrow in the middle
    screen.blit(arrow, (850, 510))


    # blits the circles to screen
    screen.blit(circle, (1025,505))
    screen.blit(circle2, (1025,585))

    try:
        if emergency is False:
            emergencybuttonscreen = screen.blit(emergencyButton, (825, 360))
            unlockButton = screen.blit(unlocked, (1025,360))
            print( imageName + " blitted to position " , position)
            if lock is False:
                unlockButton = screen.blit(unlocked, (1025,360))  
                if movement == 'forward':
                    screen.blit(pygame.image.load(image), position)
                    print( imageName + " blitted to position " , position)
                elif movement == 'backward':
                    screen.blit(pygame.image.load(image), position)
                    print( imageName + " blitted to position " , position)
                elif movement == 'left':
                    screen.blit(pygame.image.load(image), position)
                    print( imageName + " blitted to position " , position)
                elif movement == 'right':
                    screen.blit(pygame.image.load(image), position)
                    print( imageName + " blitted to position " , position)
                elif movement == 'up':
                    screen.blit(pygame.image.load(image), position)
                    print( imageName + " blitted to position " , position)
                elif movement == 'down':
                    screen.blit(pygame.image.load(image), position)
                    print( imageName + " blitted to position " , position)
                if movement == 'forwardLeft' :
                    screen.blit(pygame.image.load(image), position)
                    print( imageName + " blitted to position " , position)
                elif movement == 'forwardRight' :
                    screen.blit(pygame.image.load(image), position)
                    print( imageName + " blitted to position " , position)
                elif movement == 'backwardLeft' :
                    screen.blit(pygame.image.load(image), position)
                    print( imageName + " blitted to position " , position)
                elif movement == 'backwardRight' :
                    screen.blit(pygame.image.load(image), position)
                    print( imageName + " blitted to position " , position)  
            else:
                unlockButton = screen.blit(locked, (1025,360))  
                if movement == 'forward':
                    screen.blit(pygame.image.load(image), position)
                    print( imageName + " blitted to position " , position)
                elif movement == 'backward':
                    screen.blit(pygame.image.load(image), position)
                    print( imageName + " blitted to position " , position)
                elif movement == 'left':
                    screen.blit(pygame.image.load(image), position)
                    print( imageName + " blitted to position " , position)
                elif movement == 'right':
                    screen.blit(pygame.image.load(image), position)
                    print( imageName + " blitted to position " , position)
                elif movement == 'up':
                    screen.blit(pygame.image.load(image), position)
                    print( imageName + " blitted to position " , position)
                elif movement == 'down':
                    screen.blit(pygame.image.load(image), position)
                    print( imageName + " blitted to position " , position)
                if movement == 'forwardLeft' :
                    screen.blit(pygame.image.load(image), position)
                    print( imageName + " blitted to position " , position)
                elif movement == 'forwardRight' :
                    screen.blit(pygame.image.load(image), position)
                    print( imageName + " blitted to position " , position)
                elif movement == 'backwardLeft' :
                    screen.blit(pygame.image.load(image), position)
                    print( imageName + " blitted to position " , position)
                elif movement == 'backwardRight' :
                    screen.blit(pygame.image.load(image), position)
                    print( imageName + " blitted to position " , position)           
        elif emergency is True:
            unlockButton = screen.blit(locked, (1025,360))
            emergencybuttonscreen = screen.blit(siren, (825 , 360))
            print( imageName + " blitted to position " , position)
        else:
            print("hey")    
    except Exception as e:
       print("error", e)   

    
    # if user presses quit the application closes.
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True

    # updates the display
    pygame.display.flip() 
pygame.quit()
