import os.path
from json import loads, dumps
from random import choice
"""
name = "DKJSD01.m"

if not os.path.isfile(name):
    memory_file = open(name, "w")
    memory_file.close()
    memory = {
        "step": 1,
        "directions": "up",
    }
else:
    memory_file = open(name, "r")
    memory = loads(memory_file.read())
    memory_file.close()

print(memory["step"])
"""
s = [
    [1, 3, 0, 1, 1, 0],
    [0, 0, 156, 0, 0, 0],
    [0, 1, 0, 1, 0, 0]
]


# Память

def make_choice(x, y, map):
    X = len(map)
    Y = len(map[0])
    i = 0
    y = 0
    a = [map[i][y] for i in range(x + 1, X)]
    b = [map[i][y] for i in range(x-1, -1, -1)]
    c = [map[i][y] for y in range(y + 1, Y)]
    d = [map[i][y] for y in range(y-1, -1, -1)]
   # memory['step'] += 1
    if sum(a)>0:
        ans = 'fire_right'
    elif sum(b) > 0:
        ans = 'fire_left'
    elif sum(c) > 0:
        ans = 'fire_up'
    elif sum(d) > 0:
        ans = 'fire_down'
    else:
        ans = ans = choice(["fire_left", "fire_right", "fire_up", "fire_down"])
    

    #memory_file = open(name, "w")
    #memory_file.write(dumps(memory))
    #memory_file.close()
    
    return ans
print(make_choice(2, 3, s))
