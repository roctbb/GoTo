import random

m = [[0,0,0,0,0],
     [0,0,0,0,0],
     [0,0,1,0,0],
     [0,0,0,0,0],
     [0,0,1,0,0]]

def make_choice (x,y,m):
    for i in range(x+1, len(m)):
        if m[i][y] != 0:
            return "fire_right"
    for i in range(0, x):
        if m[i][y] != 0:
            return "fire_left"
    for i in range(0, y):
        if [x][i] != 0:
            return "fire_up"
    for i in range(y+1, len(m[0])):
        if [x][i] != 0:
            return "fire_down"
        
    return random.choice(["move_right","move_left",
                             "move_up","move_down"])
