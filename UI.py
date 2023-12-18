from All_views.view1 import draw_view1
from All_views.view2 import draw_view2
import pygame
pygame.init()

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

# the while loop..
while not exit:
    # Fills the background with blue color
    screen.fill(blueDeFrance)

    # blits the views to the screen. the parameters are the x and y coordinates.
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

    screen.blit(resized_boat_view1, (200, 255))

    rope_height = draw_view1(screen, rope_height, font, text_color)
    draw_view2(screen, shore_x, shore_y, resized_boat_view2, )
    shore_x, shore_y, resized_boat_view2, _, _, _, _, _ = draw_view2(screen, shore_x, shore_y, resized_boat_view2)

    # if user presses quit the application closes.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    # updates the display
    pygame.display.flip()
    clock.tick(30)
