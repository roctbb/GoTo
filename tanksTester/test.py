import random

def make_choice(x,y,field):
    if field[x][y]['history']==[]:
        return "fire_left"
    steps = len(field[x][y]['history'])
    if field[x][y]['history'][steps-1]=="fire_left":
        return "fire_down"
    if field[x][y]['history'][steps-1]=="fire_down":
        return "fire_right"
    if field[x][y]['history'][steps-1]=="fire_right":
        return "fire_up"
    if field[x][y]['history'][steps-1]=="fire_up":
        return "fire_left"