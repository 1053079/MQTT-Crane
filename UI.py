import pygame 
import os  

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
    
    # if user presses quit the application closes.
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True

    # updates the display
    pygame.display.flip() 