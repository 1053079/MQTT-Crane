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
pink = (255, 192, 203)
green = (0, 255, 0)
grey = (169,169,169)
purple = (128, 0, 128)
purple_rect = pygame.Rect(90, 50, 20, 20)
purple_speed = 1
rope_height = 110
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

    if keys[pygame.K_a] and purple_rect.left > 80:
        purple_rect.x -= purple_speed
    if keys[pygame.K_d] and purple_rect.right < 280:
        purple_rect.x += purple_speed

    screen.fill(black)

    # Your drawings (x, y, width, height)
    pygame.draw.rect(screen, red, [200, 150, 200, 10])  # Shore
    pygame.draw.rect(screen, red, [205, 145, 10, 110])  # Shore
    pygame.draw.rect(screen, red, [385, 145, 10, 110])  # Shore
    pygame.draw.rect(screen, yellow, [240, 30, 10, 120])  # Crane_Leg
    pygame.draw.rect(screen, yellow, [80, 40, 200, 10])  # Bridge
    pygame.draw.rect(screen, purple, purple_rect)  # Crane_Cabin
    pygame.draw.rect(screen, grey, [0, 250, 800, 50])   # waterline
    pygame.draw.line(screen, purple, (purple_rect.centerx, purple_rect.bottom),(purple_rect.centerx, purple_rect.bottom + rope_height), 5)
    pygame.draw.polygon(screen, orange, [(50, 200), (100, 250), (150, 200)])  # Boat triangle
    pygame.draw.rect(screen, green, [55, 185, 40, 15])  # Container 1
    pygame.draw.rect(screen, blue, [105, 185, 40, 15])  # Container 2




# Update the display
    pygame.display.flip()

    clock.tick(60)