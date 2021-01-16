import bullets
import pygame
import main
# set of walls currently on the map
# used_spaces = {}
placed_towers = {}
# 1 = wall
# 2 = level one turret
RED = (255, 0, 0)

class Tower:
    def __init__(self, type, x_box, y_box):
        self.type = type
        self.x_pos = x_box
        self.y_pos = y_box
        self.timer = 0

    def check_radius(self, enemy, path, current_time):
        if self.type == 2 and (current_time - self.timer) > 1:
            radius = set()
            enemy_x = enemy.path[enemy.index][0]
            enemy_y = enemy.path[enemy.index][1]
            x_aux, y_aux = 1, 1
            for i in range(7):
                if i == 0:
                    radius.add((self.x_pos+x_aux, self.y_pos+y_aux))
                if i == 1 or i == 2:
                    y_aux -= 1
                    radius.add((self.x_pos+x_aux, self.y_pos+y_aux))
                if i == 3 or i == 4:
                    x_aux -= 1
                    radius.add((self.x_pos+x_aux, self.y_pos+y_aux))
                if i == 5 or i == 6:
                    y_aux += 1
                    radius.add((self.x_pos+x_aux, self.y_pos+y_aux))
            radius.add((self.x_pos, self.y_pos+1))
            # print(radius)
            new_radius = set()
            for coords in radius:
                if coords in path:
                    new_radius.add(coords)
            if (enemy_x, enemy_y) in new_radius:
                # pygame.draw.circle(main.gameDisplay, RED, (100, 100), 50, 0)
                enemy.update_health()
                self.timer = current_time
                print((self.x_pos)*50 + 125,(self.y_pos)*50 + 25)
                # return(bullets.Bullet(enemy.rect.x, enemy.rect.y, 925, 325))
                return(bullets.Bullet(enemy.rect.x, enemy.rect.y, (self.x_pos)*50 + 125, (self.y_pos)*50 + 25))
                # self.rect.x = 50*self.path[self.index+1][0] + 113
                # self.rect.y = 50*self.path[self.index+1][1] + 13
        return bullets.Bullet(-1, -1, -1, -1)




def add_wall(x, y, edges, type):
    global used_spaces, wall_type, towers
    # North
    if (x, y) in placed_towers:
        None
    else:
        # used_spaces.update({(x, y): type})
        placed_towers.update({(x, y): Tower(type, x, y)})
        # for tower in placed_towers:
        #     print(tower.x_pos, tower.y_pos, tower.type, end=" ")
        # print()
        try:
            edges.remove(((x, y, ), (x, y-1)))
        except:
            None
        try:
            edges.remove(((x, y-1), (x, y)))
        except:
            None
        # East
        try:
            edges.remove(((x, y), (x+1, y)))
        except:
            None
        try:
            edges.remove(((x+1, y), (x, y)))
        except:
            None
        # South
        try:
            edges.remove(((x, y), (x, y+1)))
        except:
            None
        try:
            edges.remove(((x, y+1), (x, y)))
        except:
            None
        # West
        try:
            edges.remove(((x, y), (x-1, y)))
        except:
            None
        try:
            edges.remove(((x-1, y), (x, y)))
        except:
            None
    return edges


def remove_wall(x, y, edges, type):
    global used_spaces, wall_type
    # North
    if (x, y) in placed_towers:
        # del used_spaces[(x, y)]
        del placed_towers[(x, y)]
        # North
        if y != 0:
            edges.append(((x, y), (x, y-1)))
        else:
            None
        if y != 0:
            edges.append(((x, y-1), (x, y)))
        else:
            None
        # East
        if x != 21:
            edges.append(((x, y), (x+1, y)))
        else:
            None
        if x != 21:
            edges.append(((x+1, y), (x, y)))
        else:
            None
        # South
        if y != 12:
            edges.append(((x, y), (x, y+1)))
        else:
            None
        if y != 12:
            edges.append(((x, y+1), (x, y)))
        else:
            None
        # West
        if x != 0:
            edges.append(((x, y), (x-1, y)))
        else:
            None
        if x != 0:
            edges.append(((x-1, y), (x, y)))
        else:
            None
    else:
        None
    return edges
