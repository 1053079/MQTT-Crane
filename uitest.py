import paho.mqtt.client as mqtt
import time
import json
import pygame
import sys



client = mqtt.Client()


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

WASD = pygame.image.load('UserInterface/buttons/wasdKeys.png')

# Arrow in middle
arrow = pygame.image.load('UserInterface/buttons/arrowKey.png')

# circle buttons
circle = pygame.image.load('UserInterface/buttons/xButton.png')


circle2 = pygame.image.load('UserInterface/buttons/plusButton.png')

        
lock = False
emergency = False
movement = 'none'
speed = 'normal'
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected to broker")
    else:
        print(f"Connection failed with code {rc}")

# prints back the message received and the topic
def on_message(client, userdata,message):
    global movement, speed, lock
    print("Message received: " + str((message.payload.decode("utf-8"))))
    print("Topic is " + str(message.topic))
    
    # decodes the JSON and allows us to get the values of the movement, speed and lock.
    payload_data = json.loads(message.payload.decode('utf-8'))
    movement = payload_data.get("movement")
    speed = payload_data.get("speed")
    lock = payload_data.get("lock")
    print ("movement is " , movement)
    print ('speed is' , speed)
    print ('lock is' , lock)

connected= False
messageReceived= False

# hiveMQ URL and port for connection
broker = "2939d3617acc492aa3b3653ac474fdc0.s2.eu.hivemq.cloud"
port = 8883
username = "Admin"
password = "hMu4P6L_LAMj8t3"


# TLS (required for connection)
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# Username and password (required for connection)
client.username_pw_set(username, password)

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)
client.subscribe("inputs/joystick") ## have to be subscribed first then client loop start!
client.loop_start()
pygame.init() 
while connected!= True:
    time.sleep(0.2)
while messageReceived!= True: 
    time.sleep(0.2)

exit = False
while not exit:    
    # if user presses quit the application closes
        # Fills the background with blue color
    screen.fill(blueDeFrance)

    try:
        print("Before loading images")
        # blits the views to the screen. the parameters are the x and y coordinates.
        view = pygame.Surface([500, 300])
        view2 = pygame.Surface([500, 300])
        view3 = pygame.Surface([500, 300])

        WASD = pygame.image.load('UserInterface/buttons/wasdKeys.png')
        arrow = pygame.image.load('UserInterface/buttons/arrowKey.png')
        circle = pygame.image.load('UserInterface/buttons/xButton.png')
        circle2 = pygame.image.load('UserInterface/buttons/plusButton.png')
        print("After loading images")

        print("Before blitting images")
        screen.blit(view, (75, 50))
        screen.blit(view2, (625, 50))
        screen.blit(view3, (75, 400))

        # Blits WASD Keys
        screen.blit(WASD, (650, 500))
        # BLits the arrow in the middle
        screen.blit(arrow, (850, 510))

        # blits the circles to screen
        screen.blit(circle, (1025, 505))
        screen.blit(circle2, (1025, 585))
        print("After blitting images")
    except pygame.error as e:
        print("Error loading or blitting images:", e)
        pygame.quit()
        sys.exit()

            # updates the display
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                exit = True

    pygame.display.flip()

pygame.quit() 
    
