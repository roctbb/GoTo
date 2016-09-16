#checks danger of moving each way, moves if has ability to escape danger, (smart)fires if no way to escape danger, (smart)fire if has ability to exchange hps, prefires
#todo optional sniff around move closer and camp or exch

def make_choice(x, y, map):
    from random import randrange
    
    bots_x_left = 0 #on line to the left
    closest_x_left_hp = 0
    
    bots_x_right = 0 #on line to the right
    closest_x_right_hp = 0

    bots_y_above = 0 #on line above
    closest_y_above_hp = 0 
    
    bots_y_beneath = 0 #on line beneath
    closest_y_beneath_hp = 0

    potential_threats = 0

    danger_up = 0
    bots_x_up_left = 0
    bots_x_up_right = 0
    
    danger_down = 0
    bots_x_down_left = 0
    bots_x_down_right = 0
    
    danger_left = 0
    bots_y_left_above = 0
    bots_y_left_beneath = 0
    
    danger_right = 0
    bots_y_right_above = 0
    bots_y_right_beneath = 0

    prefire_left_attitude = 0
    prefire_right_attitude = 0
    prefire_down_attitude = 0
    prefire_up_attitude = 0

#aim for best and check environment        
    for j in range(len(map[0])):
        if j != y:
            if map[x][j] != 0:
                if y < j:
                    bots_y_beneath += 1
                    if closest_y_beneath_hp != 0:
                        closest_y_beneath_hp = map[x][j]
#                        return "fire_down"
                if y > j:
                    bots_y_above += 1
                    closest_y_above_hp = map[x][j]
#                        return "fire_up"

    for i in range(len(map)):
        if i != x:
            if map[i][y] != 0:
                if x < i:
                    bots_x_right += 1
                    if closest_x_right_hp != 0:
                        closest_x_right_hp = map[i][y]
#                        return "fire_right"
                if x > i:
                    bots_x_left += 1
                    closest_x_left_hp = map[i][y]
#                        return "fire_left"
#check moving danger
    #checking move danger + current + changed_state
    if x == 0:
        danger_left = 666
    if x == len(map) - 1:
        danger_right = 666
    if y == 0:
        danger_up = 666
    if y == len(map[0]) - 1:
        danger_down = 666
            #danger_left

            
    if x > 0:
        for j in range(len(map[0])):
            if map[x-1][j] != 0:
                if j == y:
                    danger_left = 666
                if y < j:
                    bots_y_left_beneath += 1
                if y > j:
                    bots_y_left_above += 1
    danger_left += min(1, bots_y_left_beneath) + min(1, bots_y_left_above) + min(1, bots_x_left) + min(1, bots_x_right)
            #danger_right

            
    if x < len(map) - 1:
        for j in range(len(map[0])):
            if map[x+1][j] != 0:
                if j == y:
                    danger_right = 666
                if y < j:
                    bots_y_right_beneath += 1
                if y > j:
                    bots_y_right_above += 1
    danger_right += min(1, bots_y_right_beneath) + min(1, bots_y_right_above) + min(1, bots_x_left) + min(1, bots_x_right)
            #danger_up (or down)
    if y > 0:
        for i in range(len(map)):
            if map[i][y-1] != 0:
                if i == x:
                    danger_up = 666
                if x < i:
                    bots_x_up_right += 1
                if x > i:
                    bots_x_up_left += 1
    danger_up += min(1, bots_x_up_left) + min(1, bots_x_up_right) + min(1, bots_y_above) + min(1, bots_y_beneath)

        #danger_down (or up)

    if y < len(map[0]) - 1:
        for i in range(len(map)):
            if map[i][y+1] != 0:
                if i == x:
                    danger_down = 666
                if x < i:
                    bots_x_down_right += 1
                if x > i:
                    bots_x_down_left += 1
    danger_down += min(1, bots_x_down_left) + min(1, bots_x_down_right) + min(1, bots_y_above) + min(1, bots_y_beneath)

        
#threats check and find best move
        #todo -- if threats are less then hp shooting system
#####BATTLE_SYSTEM_ITSELF
    potential_threats = min(1, bots_x_left) + min(1, bots_x_right) + min(1, bots_y_above) + min(1, bots_y_beneath)
    if potential_threats >= map[x][y]:
            
            #bezishodnost
            
        if min(danger_left, danger_right, danger_up, danger_down) >= map[x][y]:
                
            if closest_x_left_hp == 1:
                return "fire_left"
            if closest_x_right_hp == 1:
                return "fire_right"
            if closest_y_above_hp == 1:
                return "fire_up"
            if closest_y_beneath_hp == 1:
                return "fire_down"
                
            if bots_x_left != 0:
                return "fire_left"
            if bots_x_right != 0:
                return "fire_right"
            if bots_y_above != 0:
                return "fire_up"
            if bots_y_beneath != 0:
                return "fire_down"
                
            #neo uvoroti yeaaa
                
        if (danger_left <= danger_right) and (danger_left <= danger_up) and (danger_left <= danger_down):
            return "go_left"

        if (danger_right <= danger_left) and (danger_right <= danger_up) and (danger_right <= danger_down):
            return "go_right"

        if (danger_up <= danger_left) and (danger_up <= danger_right) and (danger_up <= danger_down):
            return "go_up"

        if (danger_down <= danger_left) and (danger_down <= danger_right) and (danger_down <= danger_up):
            return "go_down"
            #smart shoot as usual if know that he wont die
    if closest_x_left_hp == 1:
        return "fire_left"
    if closest_x_right_hp == 1:
        return "fire_right"
    if closest_y_above_hp == 1:
        return "fire_up"
    if closest_y_beneath_hp == 1:
        return "fire_down"
            
    if bots_x_left != 0:
        return "fire_left"
    if bots_x_right != 0:
        return "fire_right"
    if bots_y_above != 0:
        return "fire_up"
    if bots_y_beneath != 0:
        return "fire_down"

        #counts prefire attitudes
    prefire_left_attitude = bots_x_up_left + bots_x_down_left
    prefire_right_attitude = bots_x_up_right + bots_x_down_right
    prefire_up_attitude = bots_y_left_above + bots_y_right_above
    prefire_down_attitude = bots_y_left_beneath + bots_y_left_beneath

        #prefires smart(not really)
        
    if prefire_left_attitude == 1:
        return "fire_left"
    if prefire_right_attitude == 1:
        return "fire_right"
    if prefire_up_attitude == 1:
        return "fire_up"
    if prefire_down_attitude == 1:
        return "fire_down"

        #prefires not smart :(

    if prefire_left_attitude > 0:
        return "fire_left"
    if prefire_right_attitude > 0:
        return "fire_right"
    if prefire_up_attitude > 0:
        return "fire_up"
    if prefire_down_attitude > 0:
        return "fire_down"
        #random run around
    dirr = randrange(1,5)
    if dirr == 1:
        if danger_left == 0:
            return "go_left"
    if dirr == 2:
        if danger_up == 0:
            return "go_up"
    if dirr == 3:
        if danger_right == 0:
            return "go_right"
    if dirr == 4:
        if danger_down == 0:
            return "go_down"
