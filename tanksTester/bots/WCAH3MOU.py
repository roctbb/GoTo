from random import choice 
def make_choice(x, y, map): 
	length = len(map) 
	height = len(map[0])  
	en_hp_right = 0 
	en_hp_l = 0 
	en_hp_up = 0 
	en_hp_down = 0 


	for i in range (x+1, length): 
		en_hp_right += map[i][y] 
	for i in range (x): 
		en_hp_l += map[i][y] 
	for i in range (y): 
		en_hp_up += map[x][i] 
	for i in range (y+1, height): 
		en_hp_down += map[x][i] 


	lines = [en_hp_down, en_hp_up, en_hp_l, en_hp_right] 


	if any(lines): 
		minimum = min([i for i in lines if i > 0]) 
		if (minimum == en_hp_down) and (en_hp_down >= 1): 
			return "fire_down" 
		elif (minimum == en_hp_up) and (en_hp_up >= 1): 
			return "fire_up" 
		elif (minimum == en_hp_l) and (en_hp_l >= 1): 
			return "fire_left" 
		elif (minimum == en_hp_right) and (en_hp_right >= 1): 
			return "fire_right"
	else:
		return choice(['go_up', 'go_down', 'go_left', 'go_right']) 