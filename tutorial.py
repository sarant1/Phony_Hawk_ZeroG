import pygame, sys
from Phony_Hawk_Zergo import *

def play_tutorial():
    while True:
        # blit 2 images to cover the full size of screen for bg

        for i in range(2):
            screen.blit(bg, (i * bg.get_width() + scroll, 0))
        
        scroll -= 3

        # if scroll becomes greater than the width of bg, then it will reset scroll to 0, placing image at end of screen

        if abs(scroll) > bg.get_width():
            scroll = 0

        # for user input and player movement
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and p.pos.top > 0:
            p.pos[1] -= player_speed
        if keys[pygame.K_s] and p.pos.bottom < screen_height:
            p.pos[1] += player_speed
        if keys[pygame.K_a] and p.pos.left > 0:
            p.pos[0] -= player_speed
        if keys[pygame.K_d] and p.pos.right < screen_width:
            p.pos[0] += player_speed
        
        # blit player onto screen
        
        screen.blit(p.image, p.pos)

        # blit fireball/asteroids onto screen

        for asteroid in asteroids:
            asteroid.move()
            screen.blit(asteroid.image, asteroid.pos)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()
        pygame.display.update()

    pygame.quit()