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

# Rectangles.. or actually the views
rectangle = pygame.Surface([100,200])
rectangle2 = pygame.Surface([100,200])
rectangle3 = pygame.Surface([100,200])


# the while loop..
while not exit: 
    screen.fill(blue)
    screen.blit(rectangle,(200,200))
    screen.blit(rectangle2,(400,400))
    screen.blit(rectangle3,(600,600))
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    pygame.display.flip() 