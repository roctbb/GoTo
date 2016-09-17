def make_choice(x,y,map):
  import random
  a=random.randint(0,3)
  if a==0:
    return "fire_up"
  if a==1:
   return "fire_left"
  if a==2:
   return "fire_down"
  if a==3:
   return "fire_right"
