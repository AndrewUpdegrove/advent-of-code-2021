

x_range = (14,50)
y_range = (-267, -225)


def first_n_sum(n):
    return (n * (n+1)) / 2

# x_0: starting x pos
# t: time step integer
def x_pos(v_x0,t):
    if t == 0:
        return 0
    elif t >= v_x0:
        comp2 = 0
    else:
        comp2 = first_n_sum(v_x0-t)
    return first_n_sum(v_x0) - comp2


def y_pos(v_y0, t):
    arc_time = (2 * v_y0) + 1
    if v_y0 < 0:
        return -1 * ( first_n_sum( (-1*v_y0) + t - 1 ) - first_n_sum((-1 * v_y0) - 1) )
    elif v_y0 == 0:
        return -1 * first_n_sum(t-1)
    else:
        if t == 0:
            return 0
        elif t <= v_y0:
            return 0 # never going to actually make it to the y_range so just blow it up
        elif t <= arc_time:
            return 0 # same thing as above
        else:
            return -1 * (first_n_sum((v_y0) + (t - arc_time)) - first_n_sum(v_y0))


# Part 1
# print(first_n_sum(266))

# Test Check
'''
shot_combos = []
for j in range(-10, 12):
    for i in range(6, 31):
        for t in range(1, 22):
            end_x = x_pos(i, t)
            end_y = y_pos(j, t)
            if end_x > 30 or end_y < -10:
                break
            if end_y in range(-10, -4) and end_x in range(20, 31):
                shot_combos.append((i,j))
'''
# Part 2
shot_combos = []
for j in range(-267, 268):
    for i in range(5, 51):
        for t in range(0, 540):
            end_x = x_pos(i, t)
            end_y = y_pos(j, t)
            if end_x > 50 or end_y < -267:
                break
            if end_y in range(-267, -224) and end_x in range(14, 51):
                shot_combos.append((i,j))

shot_combos = set(shot_combos)
#shot_combos = list(shot_combos)
#shot_combos.sort(key=lambda i:i[0])
print(len(shot_combos))
#print(shot_combos)

# target area: x=14..50, y=-267..-225
