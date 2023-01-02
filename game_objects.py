import pygame, random

screen_height = 720
screen_width = 1280
player_speed = 5


class PlayerX(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/phony_hawk.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.smoothscale(self.image, (150, 150))
        self.rect.width = 150
        self.rect.height = 150

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect[1] -= player_speed
        if keys[pygame.K_s] and self.rect.bottom < screen_height:
            self.rect[1] += player_speed
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect[0] -= player_speed
        if keys[pygame.K_d] and self.rect.right < screen_width:
            self.rect[0] += player_speed

    def update(self):
        self.player_input()

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/fireball.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.smoothscale(self.image, (80, 80))
        self.image = pygame.transform.rotate(self.image, 310)
        self.rect.x = screen_width
        self.rect.y = random.randint(150, 1050)
        self.speed = -random.randint(3, 7)
    def move(self):
        self.rect = self.rect.move(self.speed, 0)
    def update(self):
        self.move()