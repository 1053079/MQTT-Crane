
# view1.py

import pygame
from pygame.font import Font
pygame.font.init()


# Set up colors
black = (0, 0, 0)
blue = (0, 0, 255)
yellow = (255, 192, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
grey = (169, 169, 169)
purple = (128, 0, 128)
dark_green = (1, 50, 32)

# Set up Rects
Cabin = pygame.Rect(225, 100, 20, 20)
movement_speed = 1
rope_height = 110
container_picked_up = False
leg_bridge = pygame.Rect(330, 200, 115, 10)
Shore_leg1 = pygame.Rect(345, 190, 10, 110)
Shore_leg2 = pygame.Rect(425, 190, 10, 110)
Crane_Leg = pygame.Rect(385, 80, 10, 120)
Bridge = pygame.Rect(225, 90, 200, 10)
Container_1 = pygame.Rect(230, 245, 40, 15)
Waterline = pygame.Rect(75, 300, 250, 50)
shore = pygame.Rect(325, 300, 250, 50)

#set up spreader
spreader_width = 10
spreader_height = 10
spreader_distance = 1

font = pygame.font.Font(None, 20)
text_color = white = (255, 255, 255)
def draw_view1(screen, rope_height, font, text_color):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and rope_height > 10:
            rope_height -= 1
        if keys[pygame.K_DOWN] and rope_height < 180:
            rope_height += 1

        if keys[pygame.K_a] and Cabin.left > 225:
            Cabin.x -= movement_speed
        if keys[pygame.K_d] and Cabin.right < 425:
            Cabin.x += movement_speed


        # Your drawings (x, y, width, height)
        pygame.draw.rect(screen, yellow, leg_bridge)
        pygame.draw.rect(screen, yellow, Shore_leg1)
        pygame.draw.rect(screen, yellow, Shore_leg2)
        pygame.draw.rect(screen, yellow, Crane_Leg)
        pygame.draw.rect(screen, yellow, Bridge)
        pygame.draw.rect(screen, purple, Cabin)
        pygame.draw.rect(screen, blue, Waterline)

        pygame.draw.rect(screen, grey, shore)

        pygame.draw.line(screen, purple, (Cabin.centerx, Cabin.bottom), (Cabin.centerx, Cabin.bottom + rope_height),5)  # Rope
        pygame.draw.rect(screen, dark_green, Container_1)

        spreader_x = Cabin.centerx - spreader_width // 2
        spreader_y = Cabin.bottom + rope_height + spreader_distance
        pygame.draw.rect(screen, yellow, (spreader_x, spreader_y, spreader_width, spreader_height))

        # Show spreader location
        spreader_location_text = font.render(f"Spreader Location: ({spreader_x}, {spreader_y})", True, text_color)
        screen.blit(spreader_location_text, (75, 65))


        return rope_height
