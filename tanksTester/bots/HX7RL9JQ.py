from random import randrange
def make_choice(x,y,map):
    ans=0
    g = randrange(1,8)
    if g == 1:
        ans = 'go_up'
    if g == 2:
        ans = 'go_left'
    if g == 3:
        ans = 'go_right'
    if g == 4:
        ans = 'go_down'
    if g == 5:
        ans = 'fire_up'
    if g == 6:
        ans = 'fire_down'
    if g == 7:
        ans = 'fire_left'
    if g == 8:
        ans = 'fire_right'
    return (ans)
    
    
