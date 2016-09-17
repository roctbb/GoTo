import random

def make_choice(x, y, tempest):

    len_map_x = len(tempest)
    len_map_y = len(tempest[0])
    
    choice_list = ["fire_up", "fire_down", "fire_right"]
    
    while x > 0:
        for i in range(x+1, len_map_x):
            if tempest[i][y] > 0:
                return "fire_right"
        for j in range(0, x):
            if tempest[i][y] > 0:
                return "fire_left"
        for i in range(y+1, len_map_y):
            if tempest[x][i] > 0:
                return "fire_down"
        for j in range(0, y):
            if tempest[x][i] > 0:
                return "fire_up"
        return "go_left"

    for i in range(x+1, len_map_x):
        if tempest[i][y] > 0:
            return "fire_right"
    for i in range(y+1, len_map_y):
        if tempest[x][i] > 0:
            return "fire_down"
    for j in range(0, y):
        if tempest[x][i] > 0:
            return "fire_up"
    c = random.choice(choice_list)
    return c
