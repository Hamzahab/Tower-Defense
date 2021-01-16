# Enemy sprites
import pygame
import main
# Window properties
WIDTH = 1200
HEIGHT = 800
FPS = 60
SPRITE_WIDTH = 25

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# # initialize pygame and create window
# pygame.init()
# pygame.mixer.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# main.gameDisplay.fill(WHITE)
# # main.draw_background()
# pygame.display.set_caption("Testing")
# clock = pygame.time.Clock()
#


class Enemy(pygame.sprite.Sprite):
    def __init__(self, path, speed):
        pygame.sprite.Sprite.__init__(self)
        self.path = path
        self.image = pygame.Surface((25, 25))
        self.color = GREEN
        self.rect = self.image.get_rect()
        # self.offset = random.randrange(1, 10)
        self.image.fill(self.color)
        self.rect.x = WIDTH - 37
        self.rect.y = 313
        self.speed = 3
        self.health = 50
        self.index = 0
        self.distance_counter = 0
        # pygame.time.delay(random.randrange(10, 60))


    def update(self):
        self.image.fill(self.color)

        if self.index == len(self.path)-1:
            self.health = 0
            self.health_bar(RED)
            self.update_health()
            # decrease player life
            main.update_player_health()
            # print(main.user_health)

        else:
            # moving to the left (x coordinate)
            # if previous x and current are the same, do nothing
            if self.path[self.index+1][0] == self.path[self.index][0]:
                pass
            else:
                self.rect.x += (self.speed)*(self.path[self.index+1][0] - self.path[self.index][0])
                self.distance_counter += self.speed

            # moving in the y direction
            if self.path[self.index+1][1] == self.path[self.index][1]:
                pass
            # is y coordinate increasing? then add it
            else:
                self.rect.y += (self.speed)*(self.path[self.index+1][1] - self.path[self.index][1])
                self.distance_counter += self.speed

            if self.distance_counter >= 50:
                self.rect.x = 50*self.path[self.index+1][0] + 113
                self.rect.y = 50*self.path[self.index+1][1] + 13
                self.distance_counter = 0
                self.index += 1

    def update_health(self):
        # if there is still some health left
        if self.health > 25:
            self.health_bar(GREEN)
            self.health -= 25
        # if at half health, turn yellow
        elif self.health <= 25 and self.health > 0:
            self.health_bar(YELLOW)
            self.health -= 25
        # if no more health remaining, remove the sprite
        else:
            self.color = RED
            # deletes sprite from the screen
            self.kill()


    # simply changes color of enemy
    def health_bar(self, h_color):
        self.color = h_color




#
# enemy_sprites = pygame.sprite.Group()
#
#
# start_time = time.time()
#
# # Game loop
# running = True
# while running:
#     elapsed_time = time.time() - start_time
#     if elapsed_time > 1:
#         start_time = time.time()
#         if len(enemy_sprites) < 10:
#             m = Enemy(main. , 2)
#             enemy_sprites.add(m)
#         else:
#             pass
#
#     # run @ 60 FPS
#     clock.tick(FPS)
#     # Process input (events)
#     for event in pygame.event.get():
#         # check for closing window
#         if event.type == pygame.QUIT:
#             running = False
#
#     # bring enemies on forever
#     enemy_sprites.update()
#
#     # Draw / render
#     screen.fill(WHITE)
#     enemy_sprites.draw(screen)
#     # main.gameDisplay.fill(WHITE)
#     main.draw_background()
#     # *after* drawing everything, flip the display
#     pygame.display.flip()
#
# pygame.quit()
