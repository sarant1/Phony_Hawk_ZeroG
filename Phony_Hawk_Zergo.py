import pygame, sys
import random

pygame.init()
clock = pygame.time.Clock()
FPS = 60
player_speed = 5
fireball_speed = 5
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)

size = screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Phony Hawk ZeroG")




SPAWNFIREBALL = pygame.USEREVENT+0
pygame.time.set_timer(SPAWNFIREBALL, 3000)
meteor_list = []
class Meteor:
    def __init__(self):
        self.size = random.randint(10, 70)
        self.image = pygame.image.load("fireball.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (80, 80))
        self.image = pygame.transform.rotate(self.image, 310)
        self.pos = self.image.get_rect()
        self.pos.right = screen_width
        self.pos.top = random.randint(0, 1000)
        self.speed = -random.randint(1, 5)
    def move(self):
        self.pos = self.pos.move(self.speed, 0)

class Player:
    def __init__(self, image, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect()
        self.pos.width = 150
        self.pos.height = 150
    
# load bg image

bg = pygame.image.load("space_bg.png").convert()
bg = pygame.transform.smoothscale(bg, (1280, 720))


# load title image

game_title = pygame.image.load("title-game-menu.png").convert_alpha()

# load text for game menu

font = pygame.font.Font('freesansbold.ttf', 26)
playgame_text = font.render('Play Game', True, white)
playgame_text_rect = playgame_text.get_rect()
playgame_text_rect.center = (screen_width // 2, screen_height // 2 + 13)

# testfireball = pygame.image.load("fireball.png")
# testfireball_rect = testfireball.get_rect()
# testfireball = pygame.transform.smoothscale(testfireball, (70, 70))
run = True
asteroid_start = 0

class RollingScreen:
    
    def rolling_screen(scroll):
        
        # blit 2 images to cover the full size of screen for bg
        
        for i in range(2):
            screen.blit(bg, (i * bg.get_width() + scroll, 0))


# Adding game state
class GameState:
    def __init__(self):
        self.state = 'menu'
    def game_state(self):
        scroll = 0
        FPS = 60
        p_image = pygame.image.load("phony_hawk.png").convert_alpha()
        p = Player(p_image, player_speed)
        p.image = pygame.transform.smoothscale(p.image, (150, 150))
        clock = pygame.time.Clock()

        

        while self.state == 'menu':
            screen.blit(bg, (0, 0))

            screen.blit(game_title, (((screen_width/2 - game_title.get_width() / 2), 150)))
            
            playgame_rect = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(screen_width/2-125, 350, 250, 45), 2)
            screen.blit(playgame_text, playgame_text_rect)
            
            if playgame_rect.collidepoint(pygame.mouse.get_pos()):
                playgame_rect = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(screen_width/2-125, 350, 250, 45))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.state = 'tutorial'
                        self.game_state()
                        
                

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()
                    sys.quit()

            pygame.display.flip()

        if self.state == 'tutorial':
            launch_comets_tutorial = pygame.USEREVENT+1
            time = 0
            x = 0
            interval = 100
            while self.state == 'tutorial':
                clock.tick(FPS)
                RollingScreen.rolling_screen(scroll)
                scroll -= 1
                if abs(scroll) > bg.get_width():
                    scroll = 0
                # Blit player to screen

                screen.blit(p.image, p.pos)
                # screen.blit(testfireball, testfireball_rect)
                for f in meteor_list:
                    f.move()
                    screen.blit(f.image, f.pos)
                # User input movement

                keys = pygame.key.get_pressed()
                if keys[pygame.K_w] and p.pos.top > 0:
                    p.pos[1] -= player_speed
                if keys[pygame.K_s] and p.pos.bottom < screen_height:
                    p.pos[1] += player_speed
                if keys[pygame.K_a] and p.pos.left > 0:
                    p.pos[0] -= player_speed
                if keys[pygame.K_d] and p.pos.right < screen_width:
                    p.pos[0] += player_speed

                # launch the fireballs!
                
                print(pygame.time.get_ticks())
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.QUIT()
                        sys.quit()
                    if event.type == SPAWNFIREBALL:
                        x = Meteor()
                        meteor_list.append(x)
                pygame.display.update()
                pygame.display.flip()

                
play_game = GameState()

while run:
    clock.tick(FPS)

    play_game.game_state()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()