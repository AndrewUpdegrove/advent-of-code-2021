import sys
import math
import numpy as np

with open(sys.argv[1], 'r') as in_file:
    timer_list = list(map(int, in_file.readline().rstrip().split(',')))



class PopGrowth(dict):

    def __missing__(self, pair):
        if not isinstance(pair, tuple):
            raise ValueError()
        timer, days = pair
        # Base Case
        if timer >= days:
            self[pair] = 1
            return 1
        
        # Recursive Calls
        if timer == 0:
            val = self[pair] = self[(6, days-1)] + self[(8, days-1)]
        else:
            val = self[pair] = self[(timer-1, days-1)]
        return val


population = PopGrowth()
total = 0
for init_fish in timer_list:
    total += population[(init_fish, 256)]

print(total)
        
