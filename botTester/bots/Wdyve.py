from random import*
name='Brigadir'
def step (history):
    a=len(history)-1
    if a>4 and history[a][0]==history[a-1][0] and history[a-1][0]==history[a-2][0]:
        if history[a][0]=='камень':
            return 'бумага'
        elif history[a][0]=='бумага':
            return 'ножницы'
        elif history[a][0]=='ножницы':
            return 'камень'
    else:
        if len(history) % 5==0:
            return 'бумага'
        elif len(history) % 4==0:
            return 'камень'
        elif len(history) % 3==0:
            return 'бумага'
        elif len(history) % 2==0:
            return 'ножницы'
        else:
            return 'камень'












              
  

              
