import pygame 
import os  

# Initialize pygame
pygame.init() 
  
# Creates the screen allows you to change the (Width, Height) in px.
screen = pygame.display.set_mode((1200, 800)) 

# This is the title of the screen you see above the screen.
pygame.display.set_caption("Elephant Crane") 
exit = False

# Colours that we can use for visualisation
white = (255,255,255),
black = (0,0,0),
blue = (0,0,255)

# The screens.. parameters are [Width, Height]
view = pygame.Surface([500,300])
view2 = pygame.Surface([500,300])
view3 = pygame.Surface([500,300])

# Controls

# WASD arrows
WASD = pygame.image.load('UserInterface/wasdKeys.png')

# Arrow in middle
arrow = pygame.image.load('UserInterface/arrowKey.png')

# circle buttons
circle = pygame.Surface((60,60), pygame.SRCALPHA)
drawCircle = pygame.draw.circle(circle, white, (30,30), 30)

circle2 = pygame.Surface((60,60), pygame.SRCALPHA)
drawCircle2 = pygame.draw.circle(circle2, white, (30,30), 30)

# the while loop..
while not exit: 
    # Fills the background with blue color
    screen.fill(blue)

    # blits the views to the screen. the parameters are the x and y coordinates.
    screen.blit(view, (75,50)) 
    screen.blit(view2, (625,50))
    screen.blit(view3, (75,400))
    
    # Blits WASD Keys
    screen.blit(WASD, (650, 500))

    # BLits the arrow in the middle
    screen.blit(arrow, (850, 500))

    # blits the circles to screen
    screen.blit(circle, (1025,500))
    screen.blit(circle2, (1025,575))
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    pygame.display.flip() 