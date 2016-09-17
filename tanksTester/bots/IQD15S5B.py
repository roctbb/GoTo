import random
def make_choice(x, y, o):
    p1='-'
    p2='-'
    for i in o:
        one=[]
        if i[y]==1:
            one.append(i[y])
    if len(one)>1:
        p1='+'
    for y in i:
        two=[]
        if y==1:
            two.append(y)
    if len(two)>1:
        p2='+'
    if p1==p2 and p1=='+':
        if x[y+1:].count(1)!=0:
            return 'fire_right'
        elif x[:y].count(1)!=0:
            return 'fire_left'
        elif i<x and i[y].count(1)!=0:
            return 'fire_up'
        elif i>x and i[y].count(1)!=0:
            return 'fire_down'
    elif p1=='+' and p2!='+':
        for i[y+1] in o:
            one1=[]
            if i[y+1]==1:
                one1.append(i[y+1])
        if len(one1)==0:
            return 'go_right'
        for i[y-1] in o:
            two1=[]
            if i[y-1]==1:
                two1.append(i[y-1])
        if len(two1)==0:
            return 'go_left'
        else:
            one1=[]
            for i in o:
                while i<x:
                    if i[y]==1:
                        one1.append(y)
            if len(one1)!=0:
                return 'fire_up'
            else:
                return 'fire_down'
    elif p1!='+' and p2=='+':
        if o[x+1].count(1)==0:
            return 'go_down'
        elif o[x-1].count(1)==0:
            return 'go_up'
        else:
            if x[:y].count(1)!=0:
                return 'fire_right'
            else:
                return 'fire_left'
    else:   
        return random.choice(['fire_up', 'fire_down', 'fire_left', 'fire_right'])
