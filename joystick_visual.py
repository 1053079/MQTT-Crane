import pygame

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Dit zijn de variabelen voor de afbeeldingen
arrow_up = pygame.image.load('afbeeldingen/arrow_up.png').convert_alpha()
arrow_down = pygame.image.load('afbeeldingen/arrow_down.png').convert_alpha()
arrow_left = pygame.image.load('afbeeldingen/arrow_left.png').convert_alpha()
arrow_right = pygame.image.load('afbeeldingen/arrow_right.png').convert_alpha()
arrow_upstairs = pygame.image.load('afbeeldingen/arrow_upstairs.png').convert_alpha()
arrow_downstairs = pygame.image.load('afbeeldingen/arrow_downstairs.png').convert_alpha()
locked = pygame.image.load('afbeeldingen/locked.png').convert_alpha()
unlocked = pygame.image.load('afbeeldingen/unlocked.png').convert_alpha()
siren = pygame.image.load('afbeeldingen/siren.png').convert_alpha()
emergency = pygame.image.load('afbeeldingen/emergency.png').convert_alpha()

# dit definieert de  breedte en hoogte van de PNG
new_arrow_width = 100
new_arrow_height = 100

# Dit wijzigt de grootte van de PNG's
arrow_up = pygame.transform.scale(arrow_up, (new_arrow_width, new_arrow_height))
arrow_down = pygame.transform.scale(arrow_down, (new_arrow_width, new_arrow_height))
arrow_left = pygame.transform.scale(arrow_left, (new_arrow_width, new_arrow_height))
arrow_right = pygame.transform.scale(arrow_right, (new_arrow_width, new_arrow_height))
arrow_upstairs = pygame.transform.scale(arrow_upstairs, (new_arrow_width, new_arrow_height))
arrow_downstairs = pygame.transform.scale(arrow_downstairs, (new_arrow_width, new_arrow_height))
locked = pygame.transform.scale(locked, (new_arrow_width, new_arrow_height))
unlocked = pygame.transform.scale(unlocked, (new_arrow_width, new_arrow_height))
siren = pygame.transform.scale(siren, (new_arrow_width, new_arrow_height))
emergency = pygame.transform.scale(emergency, (new_arrow_width, new_arrow_height))

# Werk de breedte en hoogte variabelen bij
arrow_width = new_arrow_width
arrow_height = new_arrow_height

# Positie van de afbeeldingen
arrow_up_rect = arrow_up.get_rect(topleft=(SCREEN_WIDTH // 2 - arrow_width // 2, SCREEN_HEIGHT - arrow_height * 2))
arrow_down_rect = arrow_down.get_rect(topleft=(SCREEN_WIDTH // 2 - arrow_width // 2, SCREEN_HEIGHT - arrow_height))
arrow_left_rect = arrow_left.get_rect(topleft=(SCREEN_WIDTH // 2 - arrow_width * 2.1, SCREEN_HEIGHT - arrow_height * 1.5))
arrow_right_rect = arrow_right.get_rect(topleft=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - arrow_height * 1.5))


arrow_upstairs_rect = arrow_upstairs.get_rect(topleft=(SCREEN_WIDTH // 2 + 20, SCREEN_HEIGHT - arrow_height * 3))
arrow_downstairs_rect = arrow_downstairs.get_rect(topleft=(SCREEN_WIDTH // 2 + 20, SCREEN_HEIGHT - arrow_height))

locked_rect = locked.get_rect(topleft=(SCREEN_WIDTH // 2 + 470, SCREEN_HEIGHT - arrow_height * 3))
unlocked_rect = unlocked.get_rect(topleft=(SCREEN_WIDTH // 2 + 470, SCREEN_HEIGHT - arrow_height * 2))

siren_rect = siren.get_rect(topleft=(SCREEN_WIDTH // 2 + 470, SCREEN_HEIGHT - arrow_height))
emergency_rect = emergency.get_rect(topleft=(SCREEN_WIDTH // 2 + 470, SCREEN_HEIGHT - arrow_height * 4))

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # dit zorgt voor een grijze achtergrond
    screen.fill((128, 128, 128))

    # Dit update de positie van de PNG's (pas deze aan naar wens)
    arrow_up_rect.topleft = (SCREEN_WIDTH // 2 + 320 - arrow_width // 2, SCREEN_HEIGHT - arrow_height * 2)
    arrow_down_rect.topleft = (SCREEN_WIDTH // 2 + 320 - arrow_width // 2, SCREEN_HEIGHT - arrow_height)
    arrow_left_rect.topleft = (SCREEN_WIDTH // 2 + 430 - arrow_width * 2.1, SCREEN_HEIGHT - arrow_height * 1.5)
    arrow_right_rect.topleft = (SCREEN_WIDTH // 2 + 320 , SCREEN_HEIGHT - arrow_height * 1.5)

    arrow_upstairs_rect.topleft = (SCREEN_WIDTH // 2 + 450, SCREEN_HEIGHT - arrow_height * 3)
    arrow_downstairs_rect.topleft = (SCREEN_WIDTH // 2 + 450, SCREEN_HEIGHT - arrow_height)

    # Dit zorgt ervoor dat de afbeeldingen verschijnen als de toetsen worden ingedrukt
    if keys[pygame.K_w]:
        screen.blit(arrow_up, arrow_up_rect)

    if keys[pygame.K_s]:
        screen.blit(arrow_down, arrow_down_rect)

    if keys[pygame.K_a]:
        screen.blit(arrow_left, arrow_left_rect)

    if keys[pygame.K_d]:
        screen.blit(arrow_right, arrow_right_rect)

    if keys[pygame.K_UP]:
        screen.blit(arrow_upstairs, arrow_upstairs_rect)
        
    if keys[pygame.K_DOWN]:
        screen.blit(arrow_downstairs, arrow_downstairs_rect)

    if keys[pygame.K_l]:
        screen.blit(locked, locked_rect)

    if keys[pygame.K_u]:
        screen.blit(unlocked, unlocked_rect)

    if keys[pygame.K_1]:
        screen.blit(siren, siren_rect)

    if keys[pygame.K_2]:
        screen.blit(emergency, emergency_rect)
        

    pygame.display.flip()

pygame.quit()
