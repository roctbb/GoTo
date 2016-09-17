from random import choice

def make_choice (x,y,m):
    a = choice ([1,2,3,4,5,6,7,8,9])
    if x-1 == len(m):
        ans = ("go_left")
    elif x-1 == len(m[0]):
        ans = ("go_right")
    else:
        ans = choice(["go_right","fire_left","go_left","fire_right","fire_up","fire_down"])
    if a == 4:
        ans = choice(["go_up","go_down"])
    return (ans)
    
    
