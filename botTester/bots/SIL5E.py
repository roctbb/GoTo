__author__ = 'roctbb'
import random

def step(history):
    random.seed(228)
    return random.choice(["камень", "ножницы","бумага"])