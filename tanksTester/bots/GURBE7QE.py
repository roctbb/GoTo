from random import randrange
def make_choice(x, y, map):
    #flag = 0
    length = len(map)
    height = len(map[0])
    #hp = map[x][y]
    r = randrange(4)
    kr = 0
    kl = 0
    ku = 0
    kd = 0



    for i in range (x+1, length):
        kr += map[i][y]

    for i in range (x):
        kl += map[i][y]

    for i in range (y):
        ku += map[x][i]
        
    for i in range (y+1, height):
        kd += map[x][i]

#       Добиваю тех, у кого мало hp

    fires = [kd, ku, kl, kr]

    if any(fires):
        minim = min([i for i in fires if i > 0])
                
        if (minim == kd) and (kd >= 1):
            return "fire_down"
        elif (minim == ku) and (ku >= 1):
            return "fire_up"
        elif (minim == kl) and (kl >= 1):
            return "fire_left"
        elif (minim == kr) and (kr >= 1):
            return "fire_right"
                

#       Если стрелять не в кого, двигаться к центру

    else:
        if (r == 1):
            return "go_down"
        if (r == 2):
            return "go_right"
        if (r == 3):
            return "go_up"
        if (r == 0):
            return "go_left"


#print(make_choice(1, 2, [[0, 0, 0, 2, 2, 0], [1, 2, 1, 1, 0, 0], [9, 3, 2, 1, 3, 3], [9, 3, 0, 2, 0, 3], [1, 0, 0, 0, 2, 3], [3, 3, 3, 3, 3, 2]]))
