#бот Харитонова Александра
from random import choice
name = "Эриадор Аальст"

def step(history):
    a = len(history)
    if a <= 2:
        return choice(["камень","ножницы","бумага"])
    else:
        if history[len(history) - 1][0] == "камень":
            return "бумага"
        if history[len(history) - 1][0] == "ножницы":
            return "камень"
        if history[len(history) - 1][0] == "бумага":
            return "ножницы"
        return choice(["камень","ножницы","бумага"])
    return choice(["камень","ножницы","бумага"])

