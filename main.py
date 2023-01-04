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

# add Projectilegroup

projectile_group = pygame.sprite.Group()

def spawnPlayer():
    p = pygame.sprite.GroupSingle()
    p.add(game_objects.PlayerX())
    return p
p = spawnPlayer()
isAlive = True
# load bg image

bg = pygame.image.load("images/space_bg.png").convert()
bg = pygame.transform.smoothscale(bg, (1280, 720))

# load title image

game_title = pygame.image.load("images/title-game-menu.png").convert_alpha()

# load text for game menu

font = pygame.font.Font('freesansbold.ttf', 26)
playgame_text = font.render('Play Game', True, white)
playgame_text_rect = playgame_text.get_rect()
playgame_text_rect.center = (screen_width // 2, screen_height // 2 + 13)


# blit 2 images to cover the full size of screen for bg
    
def rolling_screen(scroll):
    for i in range(2):
        screen.blit(bg, (i * bg.get_width() + scroll, 0))

# Adding game state
class GameState:

    def __init__(self):
        self.state = 'menu'

    def game_state(self):

        scroll = 0
        FPS = 60
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
                        isAlive = True
                        p.add(game_objects.PlayerX())
                        self.state = 'playgame'
                        self.game_state()
                        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()
                    sys.quit()

            pygame.display.flip()

        if self.state == 'playgame':

            launch_comets_tutorial = pygame.USEREVENT+1
            time = 0
            x = 0
            interval = 100
            SPAWNFIREBALL = 50
            while self.state == 'playgame':
                # time clock for this level
                time += 1
                clock.tick(FPS)

                rolling_screen(scroll)
                scroll -= 1
                if abs(scroll) > bg.get_width():
                    scroll = 0
                
                p.draw(screen)
                p.update(screen)
                
                

                if pygame.sprite.groupcollide(p, projectile_group, True, True):
                    projectile_group.empty()
                    isAlive = False
                    self.state = 'menu'
                    self.game_state()

                projectile_group.draw(screen)
                projectile_group.update(screen)

                if time == SPAWNFIREBALL:
                    x = game_objects.Meteor()
                    projectile_group.add(x)
                    SPAWNFIREBALL += 50
                    print("FIREBALL SPAWNED!")
                
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