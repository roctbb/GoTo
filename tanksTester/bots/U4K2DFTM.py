def make_choice(x, y, m):
    len_map_y = len(m[0])
    len_map_x = len(m)
    x_r = 0
    x_l = 0
    y_d = 0
    y_u = 0
    for i in range(x+1, len_map_x):
        if m[i][y] > 0:
            x_r +=1
            #return "fire_right"
    for j in range(0, x):
        if m[i][y] > 0:
            x_l +=1
            #return "fire_left"
    for i in range(y + 1, len_map_y):
        if m[x][i] > 0:
            y_d +=1
            #return "fire_down"
    for i in range(0, y):
        if m[x][i] > 0:
            y_u+=1
            #return "fire_up"
    if x_r > x_l and x_r > y_d and x_r > y_u:
        return "fire_right"
    if x_l > x_r and x_l > y_d and x_l > y_u:
        return "fire_left"
    if y_d > x_r and y_d > x_l and y_d > y_u:
        return "fire_down"
    if y_u > x_r and y_u > x_l and y_u > y_d:
        return "fire_up"
    return "fire_left"

