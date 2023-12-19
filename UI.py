import pygame 
import os  
import paho.mqtt.client as mqtt
import time
import json

# connects us to the MQTT client
client = mqtt.Client()

# topics that we are subscribed to
topic_inputs_joystick = "inputs/joystick"
topic_inputs_cabinEmergencyButton = "inputs/cabinEmergencyButton"
topic_outputs_actionSpreader = "outputs/actionSpreader"

movement = 'none'
lock = False
image = 'images/locked.png'
emergency = False
mqtt_message = None
position = (1025,360)
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected to broker")
    else:
        print(f"Connection failed with code {rc}")

# prints back the message received and the topic
def on_message(client, userdata,message):
    global lock, movement, speed , emergency  , mqtt_message
    if message.topic == topic_inputs_cabinEmergencyButton: # checks for topic
     print("Message received: " + str((message.payload.decode("utf-8"))))
     print("Topic is " + str(message.topic))
     payload_data = json.loads(message.payload.decode('utf-8'))
     global emergency
     emergency = payload_data.get("status")
     print(emergency)
     mqtt_message = topic_inputs_cabinEmergencyButton
     print('mqtt message',mqtt_message)
    if message.topic == topic_outputs_actionSpreader:
     print("message lock")
     payload_data = json.loads(message.payload.decode('utf-8'))
     print(payload_data)
     global lock
     lock = payload_data.get("isLocked")
    else: 
     print("Message received is " + str((message.payload.decode("utf-8"))))
     print("Topic is " + str(message.topic))
     payload_data = json.loads(message.payload.decode('utf-8'))
     movement = payload_data.get("movement") # The movement of the joystick input
     speed = payload_data.get("speed") # Speed from joystick input, we will adjust this in our payload
     mqtt_message = topic_inputs_joystick
     print('mqtt message' ,mqtt_message)

# Dit voegt de MQTT-gegevens toe:
mqtt_username = "Admin"
mqtt_password = "hMu4P6L_LAMj8t3"
mqtt_broker_address = "2939d3617acc492aa3b3653ac474fdc0.s2.eu.hivemq.cloud"
mqtt_port = 8883


client.on_connect = on_connect
client.on_message = on_message

client.tls_set(cert_reqs=mqtt.ssl.CERT_NONE)
client.username_pw_set(mqtt_username, mqtt_password)

# Dit verbind met de MQTT-server en abonneert op het juiste onderwerp:
client.connect(mqtt_broker_address, mqtt_port)
client.subscribe([(topic_inputs_joystick, 0) , (topic_inputs_cabinEmergencyButton, 0), (topic_outputs_actionSpreader, 0)])
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
locked = pygame.image.load('VisualizationImages/locked.png').convert_alpha()
# unlocked = pygame.image.load('images/unlocked.png').convert_alpha()
# siren = pygame.image.load('images/siren.png').convert_alpha()
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


circle2 = pygame.image.load('UserInterface/buttons/plusButton.png')


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
        if mqtt_message == topic_inputs_joystick and emergency is True:
                position = (825 , 360)
                screen.blit(pygame.image.load('VisualizationImages/siren.png'), position)
                locking = screen.blit(pygame.image.load(locked), (1025, 360))
                print(  " blitted to position " , position)
        elif mqtt_message == topic_inputs_joystick or (mqtt_message == topic_inputs_cabinEmergencyButton and emergency is False):
            if lock is False:
                positionEmergency = (825, 360)
                position = (1025, 360)
                screen.blit(pygame.image.load('VisualizationImages/emergency.png'), positionEmergency)
                screen.blit(pygame.image.load('VisualizationImages/unlocked.png'), position)
                print("lock status is" , lock)
        # only does actions if its from inputs/joystick and emergency is fals
                if movement == 'forward':
                    position = (690,515)
                    screen.blit(pygame.image.load('VisualizationImages/arrow_up.png'), position)
                    print( " blitted to position " , position)
                elif movement == 'backward':
                    position = (690,590)
                    screen.blit(pygame.image.load('VisualizationImages/arrow_down.png'), position)
                    print(  " blitted to position " , position)
                elif movement == 'left':
                    position = (653,555) 
                    screen.blit(pygame.image.load('VisualizationImages/arrow_left.png'), position)
                    print(  " blitted to position " , position)
                elif movement == 'right':
                    position = (730,555)
                    screen.blit(pygame.image.load('VisualizationImages/arrow_right.png'), position)
                    print( " blitted to position " , position)
                elif movement == 'up':
                    position = (847, 450)
                    screen.blit(pygame.image.load('VisualizationImages/arrow_upstairs.png'), position)
                    print( " blitted to position " , position)
                elif movement == 'down':
                    position = (847, 630)
                    screen.blit(pygame.image.load('VisualizationImages/arrow_downstairs.png'), position)
                    print(  " blitted to position " , position)
                if movement == 'forwardLeft' :
                    position = (640 , 500)
                    screen.blit(pygame.image.load('VisualizationImages/forwardLeft.png'), position)
                    print( " blitted to position " , position)
                elif movement == 'forwardRight' :
                    position = (740 , 500)
                    screen.blit(pygame.image.load('VisualizationImages/forwardRight.png'), position)
                    print( " blitted to position " , position)
                elif movement == 'backwardLeft' :
                    position = (640, 600)
                    screen.blit(pygame.image.load('VisualizationImages/backwardLeft.png'), position)
                    print(  " blitted to position " , position)
                elif movement == 'backwardRight' :
                    position = (740, 600)
                    screen.blit(pygame.image.load('VisualizationImages/backwardRight.png'), position)
                    print( " blitted to position " , position)  
            elif lock is True: # this code allows us to have input even if lock is true.. is it needed? depends..
                positionEmergency = (825, 360)
                position = (1025, 360)
                screen.blit(pygame.image.load('VisualizationImages/emergency.png'), positionEmergency)
                screen.blit(pygame.image.load('VisualizationImages/locked.png'), position)
                print ('lock status is ' , lock)
                if movement == 'forward':
                    position = (690,515)
                    screen.blit(pygame.image.load('VisualizationImages/arrow_up.png'), position)
                    print( " blitted to position " , position)
                elif movement == 'backward':
                    position = (690,590)
                    screen.blit(pygame.image.load('VisualizationImages/arrow_down.png'), position)
                    print(  " blitted to position " , position)
                elif movement == 'left':
                    position = (653,555) 
                    screen.blit(pygame.image.load('VisualizationImages/arrow_left.png'), position)
                    print(  " blitted to position " , position)
                elif movement == 'right':
                    position = (730,555)
                    screen.blit(pygame.image.load('VisualizationImages/arrow_right.png'), position)
                    print( " blitted to position " , position)
                elif movement == 'up':
                    position = (847, 450)
                    screen.blit(pygame.image.load('VisualizationImages/arrow_upstairs.png'), position)
                    print( " blitted to position " , position)
                elif movement == 'down':
                    position = (847, 630)
                    screen.blit(pygame.image.load('images/arrow_downstairs.png'), position)
                    print(  " blitted to position " , position)
                if movement == 'forwardLeft' :
                    position = (640 , 500)
                    screen.blit(pygame.image.load('VisualizationImages/forwardLeft.png'), position)
                    print( " blitted to position " , position)
                elif movement == 'forwardRight' :
                    position = (740 , 500)
                    screen.blit(pygame.image.load('VisualizationImages/forwardRight.png'), position)
                    print( " blitted to position " , position)
                elif movement == 'backwardLeft' :
                    position = (640, 600)
                    screen.blit(pygame.image.load('VisualizationImages/backwardLeft.png'), position)
                    print(  " blitted to position " , position)
                elif movement == 'backwardRight' :
                    position = (740, 600)
                    screen.blit(pygame.image.load('VisualizationImages/backwardRight.png'), position)
                    print( " blitted to position " , position) 
        # if emergency is true we screen blit locked lock and siren
        else: 
                position = (825 , 360)
                screen.blit(pygame.image.load('VisualizationImages/siren.png'), position)
                locking = screen.blit(pygame.image.load(locked), (1025, 360))
                print(  " blitted to position " , position)
         
    except Exception as e:
        print("error", e)   

    # if user presses quit the application closes.
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
        elif event.type == mqtt_message:
            message = mqtt_message   

    # updates the display
    pygame.display.flip() 
pygame.quit()