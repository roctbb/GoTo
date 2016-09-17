from random import choice

def make_choice(x, y, map):
    #len(map)#кол-во списков

    #X = len(map)
    #Y = len(map[0])
    #if i>0 [map[i][y] for i in range(x + 1, X)]:
    #    return "fire_right"
    #if i>0 [map[i][y] for i in range(x-1, -1, -1)]:
    #    return "fire_left"
    
    s = ["fire_up", "fire_left", "fire_down", "fire_right"]
    return choice(s)
#"go_left", "go_right", "go_up","go_down",

