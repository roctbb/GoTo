# Сделал Мельников Артем
from random import randint
name = "Melnikov"

def step(history):
    bym = 34
    kam = 33
    x = 0
    n = 0

    # Смотрим еслть ли закономерности в повторениях
    if len(history) > 2:
        if history[len(history) - 1][0] == history[len(history) - 2][0] and history[len(history) - 3][0] == history[len(history) - 2][0]:
            x = 0
            n = 80
            if history[len(history) - 1][0] == "бумага":
                bym -= n//2
                kam -= n//2
            elif history[len(history) - 1][0] == "камень":
                bym += n
                kam -= n//2
            else:
                bym -= n//2
                kam += n
        elif  history[len(history) - 1][0] == history[len(history) - 2][0]:
            # Если было 2, но не 3, то все хорошо
            n = 20
            if history[len(history) - 1][0] == "бумага":
                bym += n//2
                kam -= n
            elif history[len(history) - 1][0] == "камень":
                bym += n//2
                kam += n//2
            else:
                bym -= n
                kam += n//2

        # Избавляемся от рандома противников
        if history[len(history) - 1][0] != history[len(history) - 2][0] and history[len(history) - 3][0] != history[len(history) - 2][0] and history[len(history) - 1][0] != history[len(history) - 3][0]:
            x = 1
        n = 40
        if x == 1:
                if history[len(history) - 1][0] == "бумага":
                    bym -= n
                    kam += n//2
                elif history[len(history) - 1][0] == "камень":
                    bym += n//2
                    kam -= n
                else:
                    bym += n//2
                    kam += n//2
        
        # Рассматриваем закомерности в поведении вражеского бота
        if history[len(history) - 1][0] == "бумага":
            n = 5
            if history[len(history) - 2][1] == "камень":
                bym -= n//2
                kam += n
            elif history[len(history) - 1][0] == "камень":
                if history[len(history) - 2][1] == "ножницы":
                    bym -= n//2
                    kam -= n//2
            else:
                if history[len(history) - 2][1] == "бумага":
                    bym += n
                    kam += n//2

        

    
    random_ = randint(1, 100)
    if random_ <= bym:
        answer = "бумага"
    elif random_ <= kam + bym:
        answer = "камень"
    else:
        answer = "ножницы"
    
                
    return answer



