import pygame, random

screen_height = 720
screen_width = 1280
player_speed = 5


class PlayerX(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/phony_hawk.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.inflate(90, -50)
        self.image = pygame.transform.smoothscale(self.image, (100, 124))
        self.rect.width = 100
        self.rect.height = 124

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
    def update(self, screen):
        self.player_input()
        x = (self.rect[0] + 38, self.rect[1], self.rect[2], self.rect[3])
        # pygame.draw.rect(screen, (255, 255, 255), x, 2)
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/rotated_fireball.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.smoothscale(self.image, (130, 46))
        # self.image = pygame.transform.rotate(self.image, 310)
        self.rect.width = 130
        self.rect.height = 46
        self.rect.x = screen_width
        self.rect.y = random.randint(0, 704)
        self.speed = -random.randint(3, 7)
        
    def move(self):
        self.rect = self.rect.move(self.speed, 0)
    def die(self):
        if self.rect.x < 50:
            self.kill()
    def update(self, screen):
        self.move()
        self.die()
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)