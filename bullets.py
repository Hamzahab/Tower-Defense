import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
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

fps = pygame.time.Clock()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, end_x, end_y, start_x, start_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.color = RED
        self.rect = self.image.get_rect()
        self.image.fill(self.color)
        self.rect.x = start_x
        self.rect.y = start_y
        print(start_x, start_y)
        self.end_x = end_x
        self.end_y = end_y

        if self.end_x == self.rect.x:
            self.x_dir = 0
        else:
            self.x_dir = (self.end_x - self.rect.x)/(self.end_x - self.rect.x)

        if self.end_y == self.rect.y:
            self.y_dir = 0
        else:
            self.y_dir = (self.end_y - self.rect.y)/(self.end_y - self.rect.y)

        # print(self.rect.x, self.rect.y)
        self.speed = 10

    def update(self):
        if self.rect.x == self.end_x and self.rect.y == self.end_y:
            # reached end
            self.kill()
        else:
            # print("current")
            # print(self.rect.x, self.rect.y)
            # print("end")
            # print(self.end_x, self.end_y)


            # x direction
            if self.x_dir == 0:
                pass
            else:
                self.rect.x += int((self.speed)*(self.x_dir))
                if self.x_dir > 0 and self.rect.x >= self.end_x:
                    self.rect.x = self.end_x
                elif self.x_dir < 0 and self.rect.x <= self.end_x:
                    self.rect.x = self.end_x

            # y-direction
            if self.y_dir == 0:
                pass
            else:
                self.rect.y += int((self.speed)*(self.y_dir))
                if self.y_dir > 0 and self.rect.y >= self.end_y:
                    self.rect.y = self.end_y
                elif self.y_dir < 0 and self.rect.y <= self.end_y:
                    self.rect.y = self.end_y
        # while True:
        #     pass
