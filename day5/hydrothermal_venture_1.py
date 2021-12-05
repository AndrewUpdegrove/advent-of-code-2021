import sys
import math
import re
import numpy as np

class Vent:
    def __init__(self, x_1, y_1, x_2, y_2):
        self.x1 = x_1
        self.y1 = y_1
        self.x2 = x_2
        self.y2 = y_2
        self.danger_points = []
        self.findDangerPoints()

    def findDangerPoints(self):
        if self.x1 == self.x2:
            a, b = (self.y1, self.y2) if self.y1 < self.y2 else (self.y2, self.y1)
            self.danger_points = [(self.x1, z) for z in range(a, b+1)]
        elif self.y1 == self.y2:
            a, b = (self.x1, self.x2) if self.x1 < self.x2 else (self.x2, self.x1)
            self.danger_points = [(z, self.y1) for z in range(a, b+1)]
        else:
            y_dir = 1 if self.y2 > self.y1 else -1
            x_dir = 1 if self.x2 > self.x1 else -1
            a, b = (self.x1, self.y1)
            self.danger_points.append((a,b))
            while not (a == self.x2 or b == self.y2):
                a += x_dir
                b += y_dir
                self.danger_points.append((a,b))


with open(sys.argv[1], 'r') as in_file:
    raw = [line.rstrip() for line in in_file]

vent_list = []
for line in raw:
    num_set = list(map(int, re.findall(r'\d+', line)))
    vent_list.append(Vent(num_set[0], num_set[1], num_set[2], num_set[3]))

grid_map = np.zeros((1000,1000), dtype=int)

for vent in vent_list:
    for coor in vent.danger_points:
        grid_map[coor[0]][coor[1]] += 1


counter = 0
for i in range(len(grid_map)):
    for j in range(len(grid_map[i])):
        if grid_map[i][j] > 1:
            counter += 1

print(counter)
