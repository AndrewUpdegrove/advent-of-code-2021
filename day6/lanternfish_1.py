import sys
import math

class LanternFish(object):

    @classmethod
    def reproduce(cls):
        return cls()

    def __init__(self, timer = 8):
        self.internal_timer = timer
        self.num_children = 0

    def newDay(self):
        self.internal_timer -= 1
        if self.internal_timer == -1:
            self.internal_timer = 6
            self.num_children += 1
            return LanternFish.reproduce()

with open(sys.argv[1], 'r') as in_file:
    timer_list = list(map(int, in_file.readline().rstrip().split(',')))


population = []
for ind in timer_list:
    population.append(LanternFish(ind))

for i in range(80):
    temp_pop = []
    for x in population:
        baby = x.newDay()
        if baby:
            temp_pop.append(baby)
    population.extend(temp_pop)

print(len(population))
