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
grey = (169, 169, 169)
purple = (128, 0, 128)
dark_green = (1, 50, 32)


clock = pygame.time.Clock()
# Set up Rects
Cabin = pygame.Rect(225, 100, 20, 20)
cabin_speed = 1
rope_height = 110
container_picked_up = False
leg_bridge = pygame.Rect(330, 200, 115, 10)
Shore_leg1 = pygame.Rect(345, 190, 10, 110)
Shore_leg2 = pygame.Rect(425, 190, 10, 110)
Crane_Leg = pygame.Rect(385, 80, 10, 120)
Bridge = pygame.Rect(225, 90, 200, 10)
Container_1 = pygame.Rect(230, 235, 40, 15)
Waterline = pygame.Rect(75, 300, 250, 50)
shore = pygame.Rect(325, 300, 250, 50)
original_container_1_position = Container_1.topleft
picked_up_container_position = (0, 0)


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and rope_height > 10:
        rope_height -= 1
    if keys[pygame.K_DOWN] and rope_height < 180:
        rope_height += 1

    if keys[pygame.K_a] and Cabin.left > 225:
        Cabin.x -= cabin_speed
    if keys[pygame.K_d] and Cabin.right < 425:
        Cabin.x += cabin_speed

    if keys[pygame.K_RETURN]:
        if not container_picked_up:
            if Container_1.colliderect((Cabin.centerx, Cabin.bottom + rope_height, 1, 1)):
                container_picked_up = True
                picked_up_container_position = (
                    Container_1.x - Cabin.x,
                    Container_1.y - (Cabin.bottom + rope_height),
                )
                Container_1.topleft = (3000, 15)
        else:
            container_picked_up = False
            Container_1.topleft = (
                Cabin.x + picked_up_container_position[0],
                Cabin.bottom + rope_height + picked_up_container_position[1],
            )
            screen.fill(black)

    screen.fill(black)

    # Your drawings (x, y, width, height)
    pygame.draw.rect(screen, yellow, leg_bridge)
    pygame.draw.rect(screen, yellow, Shore_leg1)
    pygame.draw.rect(screen, yellow, Shore_leg2)
    pygame.draw.rect(screen, yellow, Crane_Leg)
    pygame.draw.rect(screen, yellow, Bridge)
    pygame.draw.rect(screen, purple, Cabin)
    pygame.draw.rect(screen, blue, Waterline)
    pygame.draw.rect(screen, grey, shore)
    pygame.draw.line(screen, purple, (Cabin.centerx, Cabin.bottom), (Cabin.centerx, Cabin.bottom + rope_height),
                     5)  # Rope
    pygame.draw.polygon(screen, red, [(200, 250), (250, 300), (300, 250)])  # Boat triangle
    pygame.draw.rect(screen, dark_green, Container_1)

    if container_picked_up:
        pygame.draw.rect(
            screen,
            blue,
            (Cabin.x + picked_up_container_position[0], Cabin.bottom + rope_height + picked_up_container_position[1], 40, 15),
        )

    # Update the display
    pygame.display.flip()

    clock.tick(30)
