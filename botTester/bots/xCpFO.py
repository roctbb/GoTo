# Сделал Мельников Артем
from random import randint
name = "Typoi"

def step(history):
    if len(history) > 0:
        x = "камень"
        y = "ножницы"
        z = "бумага"
        if history[len(history) - 1][1] == x:
            return y
        elif history[len(history) - 1][1] == x:
            return z
        else:
            return x
    else:
        return x




