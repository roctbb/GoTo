#Made by Dan

from random import choice

name = "UZh1k's_mass_destroyer"

def step(history):
    a = history
    if len(a)<3:
        ch = choice (["камень","ножницы","бумага"])
    else:
        num = len(history)
        last1 = history[num-1]
        last2 = history[num-2]
        last3 = history[num-3]
        
        ch = choice (["камень","ножницы","бумага"])
        if last1[1] == "бумага" and last2[1] == "бумага" and last2[1] == "бумага":
            ch = "камень"
        if last1[1] == "камень" and last2[1] == "камень" and last2[1] == "камень":
            ch = "ножницы"
        if last1[1] == "ножницы" and last2[1] == "ножницы" and last2[1] == "ножницы":
            ch = "бумага"
            
        if last1[0] == "камень" and last2[0] == "камень" and last2[0] == "камень":
            ch = "бумага"
        if last1[0] == "бумага" and last2[0] == "бумага" and last2[0] == "бумага":
            ch = "ножницы"
        if last1[0] == "ножницы" and last2[0] == "ножницы" and last2[0] == "ножницы":
            ch = "камень"

        if last1[0] == "бумага" and last2[0] == "ножницы":
            ch = "камень"
        if last1[0] == "камень" and last2[0] == "бумага":
            ch = "ножницы"
        if last1[0] == "ножницы" and last2[0] == "камень":
            ch = "бумага"
            
    return ch
    


    
        

