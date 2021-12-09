import sys
import math
import random
import numpy as np
import time
from scipy.optimize import minimize


def brute_force(positions, gas_consume_func):
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
    current_guess = gas_consume_func(positions, hor_pos)
    while current_guess < previous:
        hor_pos += inc
        previous = current_guess
        current_guess = gas_consume_func(positions, hor_pos)

    return hor_pos, previous

def constant_gas_usage(positions, arr):
    x = arr[0]
    return sum([abs(a - x) for a in positions])

def linear_gas_usage(positions, arr):
    x = arr[0]
    return sum([sum(range(abs(a - x)  + 1)) for a in positions])

def fast_check_gas(positions):
    pass


def optimization(positions, func):
    x_low = min(positions)
    x_upp = max(positions)
    x0 = random.randint(x_low, x_upp)
    return minimize(func, [x0], method = 'Nelder-Mead', tol = .1)


with open(sys.argv[1], 'r') as in_file:
    crab_rave = list(map(int, in_file.readline().rstrip().split(',')))

x = lambda a : constant_gas_usage(crab_rave, a)
sol = optimization(crab_rave, x)
print(sol.x)
print(constant_gas_usage(crab_rave, sol.x))
print(constant_gas_usage(crab_rave, [312]))
print(constant_gas_usage(crab_rave, [313]))



"""
constant_start = time.perf_counter()
best_constant_horizontal, linear_gas_used = brute_force(crab_rave, constant_gas_usage)
linear_end = time.perf_counter()

print(f'Number of crabs: {len(crab_rave)}')
print(f'The horizontal position is: {best_constant_horizontal} and it uses {linear_gas_used} units of fuel.')
print(f'Took {linear_end-constant_start} seconds.')

incr_start = time.perf_counter()
best_increasing_horizontal, increasing_gas_used = brute_force(crab_rave, linear_gas_usage)
incr_end = time.perf_counter()
print(f'The horizontal position is: {best_increasing_horizontal} and it uses {increasing_gas_used} units of fuel.')
print(f'Took {incr_end-incr_start} seconds.')
"""



