import pygame
import time
import graph
import breadth_first_search
import towers
import enemies
import Globals
# import enemies

pygame.init()

# Window properties
display_width = 1200
display_height = 800
FPS = 30
# Colours
RED = (150, 0, 0)
LRED = (255, 0, 0)
ORANGE = (255, 69, 0)
LORANGE = (255, 97, 3)
GREEN = (0, 150, 0)
LGREEN = (0, 255, 0)
BLUE = (0, 0, 150)
LBLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (150, 0, 150)
LPURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)

smallText = pygame.font.Font("freesansbold.ttf", 20)
largeText = pygame.font.Font('freesansbold.ttf', 115)
# user_health = 100

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Maze Defense')
clock = pygame.time.Clock()


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


def display_message(text):

    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(1)


def button(msg, x, y, w, h, ic, ac, action=None, func_var=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action:
            while True:
                pygame.event.get()
                click = pygame.mouse.get_pressed()
                if click[0] == 0:
                    break
            if func_var:
                action(func_var)
            else:
                action()

    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gameDisplay.fill(WHITE)
        TextSurf, TextRect = text_objects("Maze Defense", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("START", 250, 550, 100, 50, GREEN, LGREEN, game_loop)
        button("QUIT", 650, 550, 100, 50, RED, LRED, quitgame)

        pygame.display.update()
        clock.tick(15)


def short_path(graph):
    start = (21, 6)
    end = (0, 6)
    reached = breadth_first_search.breadth_first_search(graph, (21, 6))
    path = breadth_first_search.get_path(reached, start, end)
    return path


def health_bar():
    # full health is 100
    if Globals.user_health > 75:
        bar_color = GREEN
    elif Globals.user_health > 50:
        bar_color = YELLOW
    else:
        bar_color = RED
    # drawign bar
    pygame.draw.rect(gameDisplay, bar_color, (1000, 700, Globals.user_health, 25))


def update_player_health():
    if Globals.user_health > 0:
        Globals.user_health -= 10


def game_loop():
    gameExit = False
    gameDisplay.fill(WHITE)
    draw_background()
    health_bar()

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                display_message("exit game")
                gameExit = True
                quitgame()
        button("WALL", 250, 675, 100, 50, BLUE, LBLUE, draw_wall_or_turret, 1)
        button("START", 100, 675, 100, 50, GREEN, LGREEN, send_wave)
        button("TURRET", 400, 675, 100, 50, ORANGE, LORANGE, draw_wall_or_turret, 2)
            # print(event)
        pygame.display.update()
        clock.tick(60)



def initialize_map():
    grid_width = 22
    grid_height = 13
    # get all vertices
    vertices = set()
    for y in range(grid_height):
        for x in range(grid_width):
            vertices.add((x, y))
    edges = list()
    for y in range(grid_height):
        for x in range(grid_width):
            # North
            if y == 0:
                None
            else:
                edges.append(((x, y), (x, y-1)))
            # East
            if x == 21:
                None
            else:
                edges.append(((x, y), (x+1, y)))
            # South
            if y == 12:
                None
            else:
                edges.append(((x, y), (x, y+1)))
            # West
            if x == 0:
                None
            else:
                edges.append(((x, y), (x-1, y)))
    return edges, vertices




def draw_background():
    # draw verticle line
    for x in range(23):
        pygame.draw.line(gameDisplay, BLACK, (100+50*x,0), (100+50*x,650))
    # draw horizontal line
    for y in range(14):
        pygame.draw.line(gameDisplay, BLACK, (100,50*y), (1200,50*y))
    textSurf, textRect = text_objects("S", smallText)
    # 1150,300 top left of square
    textRect.center = (1175, 325)
    gameDisplay.blit(textSurf, textRect)
    textSurf, textRect = text_objects("E", smallText)
    textRect.center = (125, 325)
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()


def draw_wall_or_turret(type):
    if type == 1:
        COLOUR = BLACK
    elif type == 2:
        COLOUR = ORANGE

    global _map, edges
    stop_drawing = False
    textSurf, textRect = text_objects("Left click place, Right click remove", smallText)
    textRect.center = (250, 750)
    pygame.draw.rect(gameDisplay, WHITE, (100, 675, 600, 50))
    gameDisplay.blit(textSurf, textRect)
    while not stop_drawing:

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        button("DONE", 250, 675, 100, 50, RED, LRED)
        if 250+100 > mouse[0] > 250 and 675+50 > mouse[1] > 675:
            if click[0] == 1:
                while True:
                    pygame.event.get()
                    click = pygame.mouse.get_pressed()
                    if click[0] == 0:
                        break
                _map = graph.Graph(vertices, edges)
                path = short_path(_map)
                if not path:
                        pygame.draw.rect(gameDisplay, WHITE, (60, 740, 400, 25))
                        textSurf, textRect = text_objects("INVALID PATH, try again", smallText)
                        textRect.center = (250, 750)
                        gameDisplay.blit(textSurf, textRect)
                else:
                    stop_drawing = True
        if mouse[0] < 100 or mouse[1] > 650:
            # not in grid
            None
        else:
            x_box = int((mouse[0] - 100)/50)
            y_box = int(mouse[1]/50)
            if (x_box == 0 and y_box == 6) or (x_box == 21 and y_box == 6):
                None
            else:
                if click[0] == 1:
                    if (x_box, y_box) in towers.placed_towers:
                        pass
                    else:
                        edges = towers.add_wall(x_box, y_box, edges, type)
                        pygame.draw.rect(gameDisplay, COLOUR, (x_box*50+100, y_box*50, 50, 50))
                        while True:
                            pygame.event.get()
                            click = pygame.mouse.get_pressed()
                            if click[0] == 0:
                                break
                if click[2] == 1:
                    if (x_box, y_box) in towers.placed_towers and type == towers.placed_towers[(x_box, y_box)].type:
                        edges = towers.remove_wall(x_box, y_box, edges, type)
                        pygame.draw.rect(gameDisplay, WHITE, (x_box*50+100, y_box*50, 50, 50))
                        while True:
                            pygame.event.get()
                            click = pygame.mouse.get_pressed()
                            if click[2] == 0:
                                break
                    else:
                        pass
        pygame.display.update()
        draw_background()
        clock.tick(60)

    pygame.draw.rect(gameDisplay, WHITE, (60, 740, 400, 25))


def send_wave():
    amount_of_enemies = 0
    path = short_path(_map)
    enemy_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    start_time = time.time()
    speed = 2
    # wave loop
    running = True
    current_towers = towers.placed_towers
    while running:
        for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    quitgame()
        elapsed_time = time.time() - start_time
        if elapsed_time > 1:
            start_time = time.time()
            if amount_of_enemies < 10:
                m = enemies.Enemy(path, speed)
                amount_of_enemies += 1
                enemy_sprites.add(m)
            else:
                pass
        if len(enemy_sprites) == 0 and amount_of_enemies > 9:
            running = False
        # run @ 60 FPS
        clock.tick(FPS)
        # bring enemies on forever

        for sprite in enemy_sprites:
            for pos, tower in current_towers.items():
                bullets.add(tower.check_radius(sprite, path, time.time()))
        enemy_sprites.update()
        bullets.update()
        # print(Globals.user_health)
        # Draw / render
        gameDisplay.fill(WHITE)
        re_draw_maze()
        health_bar()
        enemy_sprites.draw(gameDisplay)
        bullets.draw(gameDisplay)

        # main.gameDisplay.fill(WHITE)
        draw_background()

        # *after* drawing everything, flip the display
        pygame.display.flip()


def re_draw_maze():

    for tower in towers.placed_towers:
        _type = towers.placed_towers[tower].type
        # check type of tower
        if _type == 1:
            # wall
            x = tower[0]
            y = tower[1]
            pygame.draw.rect(gameDisplay, BLACK, (x*50+100, y*50, 50, 50))
        # draw
        if _type == 2:
            # wall
            x = tower[0]
            y = tower[1]
            pygame.draw.rect(gameDisplay, ORANGE, (x*50+100, y*50, 50, 50))


# global variables
edges, vertices = initialize_map()
_map = graph.Graph(vertices, edges)


if __name__ == "__main__":

    # print(short_path(_map))
    #
    # edges = add_wall(12, 6, edges)
    # _map = graph.Graph(vertices, edges)
    # print(short_path(_map))
    game_intro()
    game_loop()
    quitgame()
