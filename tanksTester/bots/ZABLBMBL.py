from random import randrange

go_right = 1
go_left = 1
go_down = 1
go_up = 1
must_avoid = []
can_follow = []
can_hunt = []
do_not_touch = []
def make_choice(x, y, мапа):
    go_right = 1
    go_left = 1
    go_down = 1
    go_up = 1
    can_attack = []
    run_from = []
    can_follow = []
    must_avoid = []
    can_assassinate = []
    can_hunt = []
    do_not_touch = []
    for i in range(len(мапа)):
        for j in range(len(мапа[i])):
            if мапа[i][j] != 0 and (i == x or j == y) and (i!=x or j!= y):
                can_attack += [[i, j]] # Что может атаковать

                
            elif мапа[i][j] != 0 and (x - i == 1
                                    or i - x == 1
                                    or y - j == 1
                                    or j - y == 1
                                    or (x == i and y - j == 1)
                                    or (x == i and j - y == 1)
                                    or (j == y and x - i == 1)
                                    or (y == j and i - x == 1)) and мапа[i][j] >= мапа[x][y]:
                must_avoid += [[i, j]] # Чего следует остерегаться

                
            elif мапа[i][j] != 0 and (x - i == 1 or i - x == 1 or y - j == 1 or j - y == 1) and мапа[i][j] < мапа[x][y]:
                can_assassinate += [[i, j]] # Что следует грохнуть незамедлительно

                
            #elif мапа[i][j] != 0 and (i == x or j == y) and (i!=x or j!= y) and мапа[i][j] > мапа[x][y]:
            #    run_from += [[i,j]] # От чего спасаться

            
            elif мапа[i][j] != 0 and ((i - x == 2 and (y - j >= 2 or j - y >= 2))
                                      or
                                      (x - i == 2 and (y - j >= 2 or j - y >= 2))
                                      or
                                      (y - j == 2 and (x - i >= 2 or i - x >= 2))
                                      or
                                      (j - y == 2 and (x - i >= 2 or i - x >= 2))
                                    ):
                can_follow += [[i,j]] # Что преследовать
            elif мапа[i][j] != 0 and (i != x or j != y) and мапа[i][j] < мапа[x][y]:
                can_hunt += [[i,j]]
            elif мапа[i][j] != 0 and (i != x or j != y) and мапа[i][j] >= мапа[x][y]:
                do_not_touch += [[i,j]]



            
    #print(can_attack) # Отладка
    #print(run_from) # Отладка
    #print(can_follow) # Отладка
    #print(must_avoid) # Отладка
    #print(can_assassinate) # Отладка
    #print(can_hunt) # Отладка
    #print(do_not_touch) # Отладка

    
    minhealth = [-1, -1, 99999999]
    for i in must_avoid:
        avoid(x, y, i[0], i[1]) # Можно ли куда-либо бегать
        
    for i in can_attack:
        if мапа[i[0]][i[1]] < minhealth[2]:
            minhealth = [i[0], i[1], мапа[i[0]][i[1]]] # Определение, кого именно грохнуть из двух целей (по мин здоровью)
    #if len(can_attack) >= 2:
        #if minhealth[2] == 1:
        return attack(x, y, minhealth[0], minhealth[1])

    
        #else:
            #return run(x, y, len(мапа), len(мапа[0]), can_attack)
    #elif len(can_attack) == 1 and мапа[can_attack[0][0]][can_attack[0][1]] < мапа[x][y]:
        #return attack(x, y, can_attack[0][0], can_attack[0][1])
    #else:
        #return run(x, y, len(мапа), len(мапа[0]), can_attack)
    for i in can_assassinate:
        return follow(x, y, i[0], i[1]) # преследовать цели
    
    min_rasst = [-1, -1, len(мапа) + len(мапа[0])]

    for i in can_hunt:
        if 0 < i[0] - x < min_rasst[2] or 0 < x - i[0] < min_rasst[2] or 0 < i[1] - y < min_rasst[2] or 0 < y - i[1] < min_rasst[2]:
            min_rasst = [i[0], i[1], i[0] - x] # Определение, за кем охотиться
            
    if len(can_hunt) != 0:
        return follow(x, y, min_rasst[0], min_rasst[1]) # Охота



    
    return "fire_up" # Если вдруг ничего не сделать, то просто пальба вверх
    
        
            

def run(x1, y1, l, h, can_attack): # Функция побега
    x2 = can_attack[0][0]
    y2 = can_attack[0][1]
    a = randrange(2)
    if x2 != 0 and y2 != 0 and x2 != l and y2 != h:
        if x2 == x1 and go_right == 1 and a == 1:
            return "go_right"
        elif go_right == 0:
            return "fire_right"
        if x2 == x1 and go_left == 1 and a == 0:
            return "go_left"
        elif go_left == 0:
            return "fire_left"
        if y2 == y1 and go_down == 1 and a == 0:
            return "go_down"
        elif go_down == 0:
            return "fire_down"
        if y1 == y2 and go_up == 1 and a == 1:
            return "go_up"
        elif go_up == 0:
            return "fire_up"
    if x2 == 0 and x2 == x1:
        return "go_right"
    if x2 == l and x2 == x1:
        return "go_left"
    if y2 == 0 and y2 == y1:
        return "go_down"
    if y2 == h and y2 == y1:
        return "go_up"
    
                                
def attack(x1, y1, x2, y2):
    if x2 == x1 and y2 > y1:
        return "fire_down"
    if x2 == x1 and y2 < y1:
        return "fire_up"
    if y1 == y2 and x1 < x2:
        return "fire_right"
    if y1 == y2 and x1 > x2:
        return "fire_left"

def follow(x1, y1, x2, y2):
    if go_right == 1 and x2 > x1:
        return "go_right"
    if go_left == 1 and x2 < x1:
        return "go_left"
    if go_down == 1 and y2 > y1:
        return "go_down"
    if go_up == 1 and y2 < y1:
        return "go_up"

def avoid(x1, y1, x2, y2):
    if x2 - x1 == 1:
        go_right = 0
    if x1 - x2 == 1:
        go_left = 0
    if y1 - y2 == 1:
        go_up = 0
    if y2 - y1 == 1:
        go_down = 0

