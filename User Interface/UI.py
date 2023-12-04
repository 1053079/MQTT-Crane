import pygame 
  
pygame.init() 
  
# Creates the canvas allows you to change the (Width, Height) in px.
canvas = pygame.display.set_mode((1000, 1000)) 

# This is the title of the canvas you see above the screen.
pygame.display.set_caption("Elephant Crane") 
exit = False
  
while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    pygame.display.update() 