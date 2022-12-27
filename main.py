import pygame, sys
import game_objects

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

meteor_list = []
 
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
        p = game_objects.Player(p_image, player_speed)
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
            SPAWNFIREBALL = 100
            while self.state == 'tutorial':

                # time clock for this level
                time += 1

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
                    if f.pos.right == 0:
                        meteor_list.remove(f)
                        del f
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
                
                print(time)

                if time == SPAWNFIREBALL:
                    x = game_objects.Meteor()
                    meteor_list.append(x)
                    SPAWNFIREBALL += 100
                    print("FIREBALL SPAWNED!")
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.QUIT()
                        sys.quit()
                pygame.display.update()
                pygame.display.flip()
        if self.state == 'level1':
            while self.state == 'level1':
                screen.blit(bg, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.QUIT()
                        sys.quit()

                pygame.display.update()
                pygame.display.flip()

           
                
play_game = GameState()

while True:
    clock.tick(FPS)

    play_game.game_state()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.quit()
    pygame.display.update()
pygame.quit()