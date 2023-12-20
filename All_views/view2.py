# view2.py

import pygame

movement_speed = 1
clock = pygame.time.Clock()

# Colours that we can use for visualisation
white = (255,255,255),
black = (0,0,0),
blue = (0,0,255)
red = (255,0,0)
yellow = (255,192,0)

# Set up Rects

shore_x = 795
shore_y = 200
Waterline_view2 = pygame.Rect(625, 300, 500, 50)
Shore_view2 = pygame.Rect(shore_x, shore_y, 110, 10)
Shore_leg1_view2 = pygame.Rect(shore_x + 10, shore_y - 10, 10, 110)
Shore_leg2_view2 = pygame.Rect(shore_x + 90, shore_y - 10, 10, 110)
Crane_Leg_view2 = pygame.Rect(shore_x + 35, shore_y - 120, 10, 120)

def draw_view2(screen,shore_x, shore_y,resized_boat):
    pygame.draw.rect(screen, yellow, Shore_view2)
    # blits the boat to screen
    screen.blit(resized_boat, (777, 255))
    pygame.draw.rect(screen, blue, Waterline_view2)
    pygame.draw.rect(screen, yellow, Shore_leg1_view2)
    pygame.draw.rect(screen, yellow, Shore_leg2_view2)
    pygame.draw.rect(screen, yellow, Crane_Leg_view2)

    keys = pygame.key.get_pressed()

    # Move Shore_view2 left and right within limits
    if keys[pygame.K_s] and shore_x > 710:
        shore_x -= movement_speed
    if keys[pygame.K_w] and shore_x < 890:
        shore_x += movement_speed

    Shore_view2.x = shore_x
    Shore_leg1_view2.x = shore_x + 10
    Shore_leg2_view2.x = shore_x + 90
    Crane_Leg_view2.x = shore_x + 50

    clock.tick(30)

    return shore_x, shore_y, resized_boat, Shore_view2, Shore_leg1_view2, Shore_leg2_view2, Crane_Leg_view2, Waterline_view2