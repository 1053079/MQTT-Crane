# view3.py

import pygame

movement_speed = 1


# Set up colors
black = (0, 0, 0)
blue = (0, 0, 255)
yellow = (255, 192, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
grey = (169, 169, 169)
purple = (128, 0, 128)
dark_green = (1,50,32)

# Movable components and possisions
cabin_x = 225
cabin_y = 545
legs_y = 500
crain_y = 550
legs_bridge1_y = 505
legs_bridge2_y = 595

def draw_view3(screen, cabin_x, cabin_y, legs_y, crain_y, legs_bridge1_y, legs_bridge2_y):
    # Movement view 3
    keys = pygame.key.get_pressed()
    # Handle movement for the cabin
    if keys[pygame.K_a]:
        cabin_x -= movement_speed
    if keys[pygame.K_d]:
        cabin_x += movement_speed
    if keys[pygame.K_w]:
        cabin_y -= movement_speed
    if keys[pygame.K_s]:
        cabin_y += movement_speed
    cabin_x = max(225, min(cabin_x, 405))
    cabin_y = max(445, min(cabin_y, 635))

    # Handle movement for the legs
    if keys[pygame.K_w]:
        legs_y -= movement_speed
    if keys[pygame.K_s]:
        legs_y += movement_speed
    legs_y = max(400, min(legs_y, 590))

    # Handle movement for the crane
    if keys[pygame.K_w]:
        crain_y -= movement_speed
    if keys[pygame.K_s]:
        crain_y += movement_speed
    crain_y = max(450, min(crain_y, 640))

    # Handle movement for the crane
    if keys[pygame.K_w]:
        legs_bridge1_y -= movement_speed
    if keys[pygame.K_s]:
        legs_bridge1_y += movement_speed
    legs_bridge1_y = max(405, min(legs_bridge1_y, 595))

    # Handle movement for the crane
    if keys[pygame.K_w]:
        legs_bridge2_y -= movement_speed
    if keys[pygame.K_s]:
        legs_bridge2_y += movement_speed
    legs_bridge2_y = max(495, min(legs_bridge2_y, 685))

    # Draw View 3
    pygame.draw.rect(screen, grey, (325, 400, 250, 300))  # Shore
    pygame.draw.rect(screen, blue, (75, 400, 250, 300))  # Water

    pygame.draw.rect(screen, red, (200, 500, 100, 150))  # boat
    pygame.draw.circle(screen, red, [250, 500], 50, 0)  # boat

    pygame.draw.rect(screen, dark_green, (230, 525, 40, 75))  # container

    pygame.draw.rect(screen, purple, (cabin_x, cabin_y, 20, 20))  # cabin
    pygame.draw.rect(screen, yellow, (225, crain_y, 200, 10))  # crain

    pygame.draw.rect(screen, yellow, (345, legs_y, 10, 110))  # legs
    pygame.draw.rect(screen, yellow, (425, legs_y, 10, 110))  # legs

    pygame.draw.rect(screen, yellow, (330, legs_bridge1_y, 115, 10))  # legs_bridge
    pygame.draw.rect(screen, yellow, (330, legs_bridge2_y, 115, 10))  # legs_bridge

    return cabin_x, cabin_y, legs_y, crain_y, legs_bridge1_y, legs_bridge2_y