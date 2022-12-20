import pygame

pygame.init()
clock = pygame.time.Clock()
FPS = 60
player_speed = 5
fireball_speed = 2

size = screen_width, screen_height = 1280, 720

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Phony Hawk ZeroG")

class Asteroid:
    def __init__(self, image, speed, height, width):
        self.image = image
        self.speed = speed
        self.height = height
        self.width = width
        self.pos = image.get_rect()
    def move(self):
        self.pos = self.pos.move(-1, 1)

# load asteroid images
asteroids = []

for x in range(10):
    fireball = pygame.image.load("fireball.png")
    fireball = pygame.transform.smoothscale(fireball, (70, 70))
    a = Asteroid(fireball, fireball_speed, 70, 70)
    a.pos.right = screen_width
    asteroids.append(a)

class Player:
    def __init__(self, image, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect()
        self.pos.width = 150
        self.pos.height = 150
    

# load player through Player Class

p_image = pygame.image.load("phony_hawk.png").convert_alpha()
p = Player(p_image, player_speed)
p.image = pygame.transform.smoothscale(p.image, (150, 150))

# load bg image

bg = pygame.image.load("space_bg.png").convert()
bg = pygame.transform.smoothscale(bg, (1280, 720))
scroll = 0

run = True
asteroid_start = 0
while run:

    clock.tick(FPS)

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
            run = False
    pygame.display.update()
pygame.quit()