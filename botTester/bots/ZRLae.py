#бот Кирилла Шведенко
import random
name = "Nagibator 228"

def step(history):
    choice = ""
    if len(history) > 3:
        last2 = history[-3:]
        if last3[0][0] == last3[1][0] == [2][0]:
            i = last3[0][0]
            if i == "ножицы":
                choice = "камень"
            if i == "бумага":
                choice = "ножницы"
            if i == "камень":
                choice = "бумага"
    if len(history) < 2:
        rand = random.randint(1, 3)
        if rand == 1:
            choice = "камень"
        if rand == 2:
            choice = "ножницы"
        if rand == 3:
            choice = "бумага"
    else:
        last = history[-1:]
        choice = last[0][0]
    return choice
