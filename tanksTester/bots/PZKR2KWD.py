from random import choice
def make_choice(x, y, map):
    X = len(map)
    Y = len (map[0])
    global i 
    if x != 0: 
        return 'go_left'
    if y != (0, len (map[0])):
        return 'go_up'
    elif x == 0:
        s = ["fire_up", "fire_left", "fire_down", "fire_right"]
        return choice (s)
    if y == (0, len (map[0])):
        return 'fire_down'
    if i % 2 == 0:
        i = i+1
        return 'fire_right'
    else:
        i = i+1
        return 'fire_up'

    
    
        
