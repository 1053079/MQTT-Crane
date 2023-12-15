import pygame

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Dit zijn de variabelen voor de images
forwardLeft = pygame.image.load('images/forwardLeft.png').convert_alpha()
forwardRight = pygame.image.load('images/forwardRight.png').convert_alpha()
backwardLeft = pygame.image.load('images/backwardLeft.png').convert_alpha()
backwardRight = pygame.image.load('images/backwardRight.png').convert_alpha()

# Dit definieert de breedte en hoogte van de PNG
new_arrow_width = 100
new_arrow_height = 100

# Dit wijzigt de grootte van de PNG's
forwardLeft = pygame.transform.scale(forwardLeft, (new_arrow_width, new_arrow_height))
forwardRight = pygame.transform.scale(forwardRight, (new_arrow_width, new_arrow_height))
backwardLeft = pygame.transform.scale(backwardLeft, (new_arrow_width, new_arrow_height))
backwardRight = pygame.transform.scale(backwardRight, (new_arrow_width, new_arrow_height))

# Werk de breedte en hoogte variabelen bij
arrow_width = new_arrow_width
arrow_height = new_arrow_height

# Positie van de images
forwardLeft_rect = forwardLeft.get_rect(topleft=(SCREEN_WIDTH // 2 - arrow_width // 2, SCREEN_HEIGHT - arrow_height * 2))
forwardRight_rect = forwardRight.get_rect(topleft=(SCREEN_WIDTH // 2 - arrow_width // 2, SCREEN_HEIGHT - arrow_height))
backwardLeft_rect = backwardLeft.get_rect(topleft=(SCREEN_WIDTH // 2 - arrow_width * 2.1, SCREEN_HEIGHT - arrow_height * 1.5))
backwardRight_rect = backwardRight.get_rect(topleft=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - arrow_height * 1.5))

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # dit zorgt voor een grijze achtergrond
    screen.fill((128, 128, 128))

    # Dit update de positie van de PNG's (pas deze aan naar wens)
    forwardLeft_rect.topleft = (SCREEN_WIDTH // 2 - arrow_width * 1.5, SCREEN_HEIGHT - arrow_height * 2.5)
    forwardRight_rect.topleft = (SCREEN_WIDTH // 2 - arrow_width * 0.5, SCREEN_HEIGHT - arrow_height * 2.5)
    backwardLeft_rect.topleft = (SCREEN_WIDTH // 2 - arrow_width * 1.5, SCREEN_HEIGHT - arrow_height * 1.5)
    backwardRight_rect.topleft = (SCREEN_WIDTH // 2 - arrow_width * 0.5, SCREEN_HEIGHT - arrow_height * 1.5)

    # Dit zorgt ervoor dat de images verschijnen als de toetsen worden ingedrukt
    if keys[pygame.K_w] and keys[pygame.K_a]:
        screen.blit(forwardLeft, forwardLeft_rect)
    if keys[pygame.K_d] and keys[pygame.K_w]:
        screen.blit(forwardRight, forwardRight_rect)
    if keys[pygame.K_a] and keys[pygame.K_s]:
        screen.blit(backwardLeft, backwardLeft_rect)
    if keys[pygame.K_d] and keys[pygame.K_s]:
        screen.blit(backwardRight, backwardRight_rect)
        

    pygame.display.flip()

pygame.quit()
