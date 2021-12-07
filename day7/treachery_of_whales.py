import sys
import math
import random
import numpy as np


def brute_force(positions, func):
    x_low = min(positions)
    x_upp = max(positions)
    hor_pos = None
    inc = 0
    if np.mean(positions) <= np.median(positions):
        hor_pos = x_low
        inc = 1
    else:
        hor_pos = x_upp
        inc = -1

    previous = math.inf
    current_guess = func(positions, hor_pos)
    while current_guess < previous:
        hor_pos += inc
        previous = current_guess
        current_guess = func(positions, hor_pos)

    return hor_pos, previous

def linear_gas_usage(positions, n):
    return sum([abs(a - n) for a in positions])

def increasing_gas_usage(positions, n):
    return sum([sum(range(abs(a - n)  + 1)) for a in positions])

def fast_check_gas(positions):
    pass
    

def optimization(positions):
    x_low = min(positions)
    x_upp = max(positions)
    x0 = random.randint(x_low, x_upp)


with open(sys.argv[1], 'r') as in_file:
    crab_rave = list(map(int, in_file.readline().rstrip().split(',')))
    
best_linear_horizontal, linear_gas_used = brute_force(crab_rave, linear_gas_usage)

print(f'The horizontal position is: {best_linear_horizontal} and it uses {linear_gas_used} units of fuel.')


best_increasing_horizontal, increasing_gas_used = brute_force(crab_rave, increasing_gas_usage)
print(f'The horizontal position is: {best_increasing_horizontal} and it uses {increasing_gas_used} units of fuel.')


