import pygame 
  
pygame.init() 
  
# Creates the screen allows you to change the (Width, Height) in px.
screen = pygame.display.set_mode((1200, 1000)) 

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

# controls

# WASD arrows
# Work in Progress...

# Arrow in middle
# Is this for adjusting the speed?

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
    screen.blit(view, (50,50)) 
    screen.blit(view2, (600,50))
    screen.blit(view3, (50,400))
    
    # blits the circles to screen
    screen.blit(circle, (1000,500))
    screen.blit(circle2, (1000,575))

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    pygame.display.flip() 