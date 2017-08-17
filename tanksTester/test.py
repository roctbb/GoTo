import random

def make_choice(x,y,field):
    try:
        for i in range(x+1, len(field)):
            if field[i][y]!=0:
                return "fire_right"
        for i in range(y+1, len(field[0])):
            if field[x][i]!=0:
                return "fire_down"
        return random.choice(["fire_right", "fire_down"])
    except:
        return "go_right"

    '''
        "go_right", "go_left", "go_up", "go_down",
        "fire_right", "fire_left", "fire_up", "fire_down",

    '''

if __name__ == '__main__':
    #проверочный код