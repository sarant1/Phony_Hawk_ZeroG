import pygame, random

screen_width = 1280


class Player:
    def __init__(self, image, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect()
        self.pos.width = 150
        self.pos.height = 150

class Meteor:
    def __init__(self):
        self.size = random.randint(10, 70)
        self.image = pygame.image.load("fireball.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (80, 80))
        self.image = pygame.transform.rotate(self.image, 310)
        self.pos = self.image.get_rect()
        self.pos.right = screen_width
        self.pos.top = random.randint(0, 1000)
        self.speed = -random.randint(3, 7)
    def move(self):
        self.pos = self.pos.move(self.speed, 0)