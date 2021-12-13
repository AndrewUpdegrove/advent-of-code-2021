import sys

# hor: horizontal position of octopus, 0 is left
# vert: vertical position of octopus, 0 is top
# el: starting energy level
class Octopus(object):
    def __init__(self, el, pos, sub):
        self.energy_level = el
        self.has_flashed = False
        self.pod = sub
        self.location = pos

    def step(self):
        self.energy_up()

    def energy_up(self):
        if not self.has_flashed:
            self.energy_level += 1
            if self.energy_level > 9:
                self.flash()

    def flash(self):
        self.has_flashed = True
        self.energy_level = 0
        self.pod.new_flash(self.location)

class Pod(dict):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.step = 0
        self.total_flashes = 0
        self.step_flashes = 0
        self.all_flash = 0
        self.max_x = 0
        self.max_y = 0

    def __str__(self):
        out = ''
        for j in range(self.max_y + 1):
            for i in range(self.max_x + 1):
                out += str(self[(i,j)].energy_level)
            out += '\n'
        return out

    def __setitem__(self, key, value):
        if key[0] > self.max_x:
            self.max_x = key[0]
        if key[1] > self.max_y:
            self.max_y = key[1]
        super().__setitem__(key, Octopus(value, key, self))

    def new_flash(self, pos):
        self.step_flashes += 1
        x, y = pos
        for i in range(-1,2):
            for j in range(-1, 2):
                dumbo = self.get((x+i,y+j))
                if dumbo:
                    dumbo.energy_up()

    def go_next(self):
        self.step_flashes = 0
        for pus in list(self.values()):
            pus.has_flashed = False
        for pus in list(self.values()):
            pus.step()
        self.step += 1
        if self.step_flashes == len(self.keys()):
            self.all_flash = self.step
        self.total_flashes += self.step_flashes
        if not self.step % 10:
            print(f"Completed step {self.step}")

with open(sys.argv[1], 'r') as in_file:
    grid = [list(map(int, list(line.rstrip()))) for line in in_file ]

cephalopods = Pod()

for y in range(len(grid)):
    for x in range(len(grid[y])):
        cephalopods[(x,y)] = grid[y][x]

# Part 1
'''
while cephalopods.step < 100:
    cephalopods.go_next()

print(f'After 100 steps, there were {cephalopods.total_flashes} flashes.')
'''
# Part 2
while not cephalopods.all_flash:
    cephalopods.go_next()

print(f'All octopuses flashed together during step {cephalopods.all_flash}')

