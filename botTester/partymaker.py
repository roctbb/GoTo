__author__ = 'roctbb'
import random

def step(history):
    a=len(history)
    if a%3==0:
        return "камень"
    if a%3==1:
        return "камень"
    if a%3==2:
        return "ножницы"