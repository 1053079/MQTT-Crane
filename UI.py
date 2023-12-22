import paho.mqtt.client as mqtt
import pygame 
import os
from All_views.view1 import draw_view1
from All_views.view2 import draw_view2
from All_views.view3 import draw_view3
import json

client = mqtt.Client()

# MQTT configurations
mqtt_broker_address = "2939d3617acc492aa3b3653ac474fdc0.s2.eu.hivemq.cloud"
mqtt_port = 8883
mqtt_username = "Admin"
mqtt_password = "hMu4P6L_LAMj8t3"
mqtt_topic_outputs_positionSpreader = "outputs/positionSpreader"
mqtt_topic_outputs_motorHoist = "outputs/motorHoist"
mqtt_topic_outputs_motorCabin = "outputs/motorCabin"
mqtt_topic_outputs_motorCrane = "outputs/motorCrane"
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
     payload_data = json.loads(message.payload.decode('utf-8'))
     global emergency
     emergency = payload_data.get("status")
     mqtt_message = topic_inputs_cabinEmergencyButton
    if message.topic == topic_outputs_actionSpreader:
     payload_data = json.loads(message.payload.decode('utf-8'))
     global lock
     lock = payload_data.get("isLocked")
    else: 
     payload_data = json.loads(message.payload.decode('utf-8'))
     movement = payload_data.get("movement") # The movement of the joystick input
     speed = payload_data.get("speed") # Speed from joystick input, we will adjust this in our payload
     mqtt_message = topic_inputs_joystick

client.tls_set(cert_reqs=mqtt.ssl.CERT_NONE)
client.username_pw_set(mqtt_username, mqtt_password)

client.on_connect = on_connect
client.on_message = on_message
# Dit verbind met de MQTT-server en abonneert op het juiste onderwerp:
client.connect(mqtt_broker_address, mqtt_port)
client.subscribe([(topic_inputs_joystick, 0) , (topic_inputs_cabinEmergencyButton, 0), (topic_outputs_actionSpreader, 0)])
client.loop()
# Initialize pygame
pygame.init()
clock = pygame.time.Clock()
# Creates the screen allows you to change the (Width, Height) in px.
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# This is the title of the screen you see above the screen.
pygame.display.set_caption("Elephant Crane")
exit = False
# Colours that we can use for visualisation
white = (255, 255, 255)
black = (0, 0, 0),
blue = (0, 0, 255)
skyBlue = (0, 255, 255)
blueDeFrance = (49, 140, 231)

# The screens.. parameters are [Width, Height]
view = pygame.Surface([500, 300])
view2 = pygame.Surface([500, 300])
view3 = pygame.Surface([500, 300])


# Dit zijn de variabelen voor de images
arrow_up = pygame.image.load('VisualizationImages/arrow_up.png').convert_alpha()
arrow_down = pygame.image.load('VisualizationImages/arrow_down.png').convert_alpha()
arrow_left = pygame.image.load('VisualizationImages/arrow_left.png').convert_alpha()
arrow_right = pygame.image.load('VisualizationImages/arrow_right.png').convert_alpha()
arrow_upstairs = pygame.image.load('VisualizationImages/arrow_upstairs.png').convert_alpha()
arrow_downstairs = pygame.image.load('VisualizationImages/arrow_downstairs.png').convert_alpha()
locked = pygame.image.load('VisualizationImages/locked.png').convert_alpha()
unlocked = pygame.image.load('VisualizationImages/unlocked.png').convert_alpha()
siren = pygame.image.load('VisualizationImages/siren.png').convert_alpha()
emergencyButton = pygame.image.load('VisualizationImages/emergency.png').convert_alpha()
forwardLeft = pygame.image.load('VisualizationImages/forwardLeft.png').convert_alpha()
forwardRight = pygame.image.load('VisualizationImages/forwardRight.png').convert_alpha()
backwardLeft = pygame.image.load('VisualizationImages/backwardLeft.png').convert_alpha()
backwardRight = pygame.image.load('VisualizationImages/backwardRight.png').convert_alpha()
emergencyButton = pygame.image.load('VisualizationImages/emergency.png').convert_alpha()

# Controls
# WASD arrows
WASD = pygame.image.load('UserInterface/buttons/wasdKeys.png')

# Arrow in middle
arrow = pygame.image.load('UserInterface/buttons/arrowKey.png')

# circle buttons
circle = pygame.image.load('UserInterface/buttons/xButton.png')
circle2 = pygame.image.load('UserInterface/buttons/plusButton.png')


rope_height = 110
container_picked_up = False
Container_1 = pygame.Rect(230, 245, 40, 15)
shore_x = 805
shore_y = 200


# boat_view1
boat_view1 = pygame.image.load('UserInterface/boat_view1.png')
new_size_view1 = (100, 50)
resized_boat_view1 = pygame.transform.scale(boat_view1, new_size_view1)


# boat_view2
boat_view2 = pygame.image.load('UserInterface/boat_view2.png')
new_size_view2 = (175, 50)
resized_boat_view2 = pygame.transform.scale(boat_view2, new_size_view2)


cabin_x = 225
cabin_y = 545
legs_y = 500
crain_y = 550
legs_bridge1_y = 505
legs_bridge2_y = 595

font = pygame.font.Font(None, 15)
text_color = (255, 255, 255)


# Movable components and possisions
cabin_x = 225
cabin_y = 545
legs_y = 500
crain_y = 550
legs_bridge1_y = 505
legs_bridge2_y = 595

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
                screen.blit(siren, position)
                locking = screen.blit(pygame.image.load(locked), (1025, 360))
        elif mqtt_message == topic_inputs_joystick or (mqtt_message == topic_inputs_cabinEmergencyButton and emergency is False):
            if lock is False:
                positionEmergency = (825, 360)
                position = (1025, 360)
                screen.blit(emergencyButton, positionEmergency)
                screen.blit(unlocked, position)
        # only does actions if its from inputs/joystick and emergency is fals
                if movement == 'forward':
                    position = (690,515)
                    screen.blit(arrow_up, position)
                elif movement == 'backward':
                    position = (690,590)
                    screen.blit(arrow_down, position)
                elif movement == 'left':
                    position = (653,555) 
                    screen.blit(arrow_left, position)
                elif movement == 'right':
                    position = (730,555)
                    screen.blit(arrow_right, position)
                elif movement == 'up':
                    position = (847, 450)
                    screen.blit(arrow_upstairs, position)
                elif movement == 'down':
                    position = (847, 630)
                    screen.blit(arrow_downstairs, position)
                if movement == 'forwardLeft' :
                    position = (640 , 500)
                    screen.blit(forwardLeft, position)
                elif movement == 'forwardRight' :
                    position = (740 , 500)
                    screen.blit(forwardRight, position)
                elif movement == 'backwardLeft' :
                    position = (640, 600)
                    screen.blit(backwardLeft, position)
                elif movement == 'backwardRight' :
                    position = (740, 600)
                    screen.blit(backwardRight, position)
            elif lock is True: # this code allows us to have input even if lock is true.. is it needed? depends..
                positionEmergency = (825, 360)
                position = (1025, 360)
                screen.blit(emergencyButton, positionEmergency)
                screen.blit(locked, position)
                if movement == 'forward':
                    position = (690,515)
                    screen.blit(arrow_up, position)
                elif movement == 'backward':
                    position = (690,590)
                    screen.blit(arrow_down, position)
                elif movement == 'left':
                    position = (653,555) 
                    screen.blit(arrow_left, position)
                elif movement == 'right':
                    position = (730,555)
                    screen.blit(arrow_right, position)
                elif movement == 'up':
                    position = (847, 450)
                    screen.blit(arrow_upstairs, position)
                elif movement == 'down':
                    position = (847, 630)
                    screen.blit(arrow_downstairs, position)
                if movement == 'forwardLeft' :
                    position = (640 , 500)
                    screen.blit(forwardLeft, position)
                elif movement == 'forwardRight' :
                    position = (740 , 500)
                    screen.blit(forwardRight, position)
                elif movement == 'backwardLeft' :
                    position = (640, 600)
                    screen.blit(backwardLeft, position)
                elif movement == 'backwardRight' :
                    position = (740, 600)
                    screen.blit(backwardRight, position)
        # if emergency is true we screen blit locked lock and siren
        else: 
                position = (825, 360)
                lockPosition = (1025, 360)
                screen.blit(siren, position)
                locking = screen.blit(locked, lockPosition)
    except Exception as e:
        print("error", e)

   
    screen.blit(resized_boat_view1, (200, 255))
    rope_height = draw_view1(screen, rope_height, font, text_color)
    draw_view2(screen, shore_x, shore_y, resized_boat_view2, )
    shore_x, shore_y, resized_boat_view2, _, _, _, _, _ = draw_view2(screen, shore_x, shore_y, resized_boat_view2)
    draw_view3(screen, cabin_x, cabin_y, legs_y, crain_y, legs_bridge1_y, legs_bridge2_y)
    cabin_x, cabin_y, legs_y, crain_y, legs_bridge1_y, legs_bridge2_y = draw_view3(screen, cabin_x, cabin_y, legs_y, crain_y, legs_bridge1_y, legs_bridge2_y)
    
    # if user presses quit the application closes.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == mqtt_message:
            message = mqtt_message   

    # updates the display
    clock.tick(30)
    pygame.display.flip() 
pygame.quit()