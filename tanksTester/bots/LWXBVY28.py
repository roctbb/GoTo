import random

def make_choice (x, y, map):
    options = ['go_up', 'go_down', 'go_left', 'go_right','fire_up', 'fire_down', 'fire_left', 'fire_right']
    return random.choice(options)
