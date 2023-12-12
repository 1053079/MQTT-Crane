import pygame
import sys
# Initialize pygame
pygame.init()

# Create a display surface
width, height = 500, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("STS Crane")

# Set up colors
black = (255, 255, 255)
blue = (0, 0, 255)
yellow = (255, 192, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
grey = (169,169,169)
purple = (128, 0, 128)

# Set up Rects
Cabin = pygame.Rect(90, 50, 20, 20)
cabin_speed = 1
rope_height = 110
container_picked_up = False
Shore = pygame.Rect(200, 150, 115, 10)
Shore_leg1 = pygame.Rect(205, 145, 10, 110)
Shore_leg2 = pygame.Rect(300, 145, 10, 110)
Crane_Leg = pygame.Rect(240, 30, 10, 120)
Bridge = pygame.Rect(80, 40, 200, 10)
Container_1 = pygame.Rect(85, 185, 40, 15)
Container_2 = pygame.Rect(135, 185, 40, 15)
Waterline = pygame.Rect(0, 250, 800, 50)
original_container_1_position = Container_1.topleft
original_container_2_position = Container_2.topleft
picked_up_container_position = (0, 0)



clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and rope_height > 10:
        rope_height -= 1
    if keys[pygame.K_s] and rope_height < 180:
        rope_height += 1

    if keys[pygame.K_a] and Cabin.left > 80:
        Cabin.x -= cabin_speed
    if keys[pygame.K_d] and Cabin.right < 280:
        Cabin.x += cabin_speed

    if keys[pygame.K_RETURN]:
        if not container_picked_up:
            if Container_1.colliderect((Cabin.centerx, Cabin.bottom + rope_height, 1, 1)):
                container_picked_up = True
                picked_up_container_position = Container_1.topleft
                Container_1.topleft = (width, height)
            elif Container_2.colliderect((Cabin.centerx, Cabin.bottom + rope_height, 1, 1)):
                container_picked_up = True
                picked_up_container_position = Container_2.topleft
                Container_2.topleft = (width, height)
        else:
            container_picked_up = False
            Container_1.topleft = original_container_1_position
            Container_2.topleft = original_container_2_position

    screen.fill(black)

    # Your drawings (x, y, width, height)
    pygame.draw.rect(screen, red, Shore)
    pygame.draw.rect(screen, red, Shore_leg1)
    pygame.draw.rect(screen, red, Shore_leg2)
    pygame.draw.rect(screen, yellow, Crane_Leg)
    pygame.draw.rect(screen, yellow, Bridge)
    pygame.draw.rect(screen, purple, Cabin)
    pygame.draw.rect(screen, grey, Waterline)
    pygame.draw.line(screen, purple, (Cabin.centerx, Cabin.bottom), (Cabin.centerx, Cabin.bottom + rope_height), 5) # Rope
    pygame.draw.polygon(screen, orange, [(80, 200), (130, 250), (180, 200)])  # Boat triangle
    pygame.draw.rect(screen, blue, Container_1)
    pygame.draw.rect(screen, blue, Container_2)

    if container_picked_up:
        pygame.draw.rect(screen, blue, (Cabin.centerx - 20, Cabin.bottom + rope_height - 15, 40, 15))

    # Update the displayddd
    pygame.display.flip()

    clock.tick(60)