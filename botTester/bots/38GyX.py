#by AlexeyTihonov
name = "mambo"
from random import choice
def step(history):
    a = 0
    b = 0
    c = 0
    i = 0
    while i < len(history):
        d = history[i][0]
        if d == 'камень':
            a = a + 1
        elif d == 'ножницы':
            b = b + 1
        else:
            c = c + 1
        i = i + 1
    if a == c and c == b:
        return choice(['камень', 'ножницы', 'бумага'])
    if a == c and b < c:
        return 'камень'
    else:
        return choice(['ножницы', 'бумага'])
    if a == b and b > c:
        return 'ножницы'
    else:
        return choice(['камень', 'бумага'])
    if b == c and b > a:
        return 'бумага'
    else:
        return choice(['ножницы', 'камень'])
    if a < b and a < c:
        return 'бумага'
    if b < a and b < c:
        return 'камень'
    else:
        return 'ножницы'
