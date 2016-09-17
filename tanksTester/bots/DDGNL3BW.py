import os.path
from json import loads, dumps
from random import choice


def make_choice(x, y, map):
    for j in range(len(map[0])):
        if j != y:
            if map[x][j] != 0:
                if y < j:
                    return "fire_down"
                if y > j:
                    return "fire_up"

 
    for i in range(len(map)):
        if i != x:
            if map[i][y] != 0:
                if x < i:
                    return "fire_right"
                if x > i:
                    return "fire_left"

    
    return choice(["go_up", "go_down", "go_left", "go_right"])

 
                   
