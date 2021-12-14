import sys
import re
import numpy as np


def fold(paper, directions):
    folded = None
    axis, pos = directions
    if axis == 'x':
        folded = np.transpose(paper)
    else:
        folded = paper.copy()

    for i in range(len(folded)-1, pos, -1):
        above = 2 * pos - i
        for j in range(len(folded[i])):
            folded[above][j] |= folded[i][j]

    folded = folded[:pos]
    if axis == 'x':
        folded = np.transpose(folded)

    return folded

coor_set = []
fold_instructions = []
max_x = 0
max_y = 0
with open(sys.argv[1], 'r') as in_file:
    for line in in_file:
        numbers = re.findall('\d+', line)
        if len(numbers) == 2:
            x = int(numbers[0])
            y = int(numbers[1])
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            coor_set.append((x,y))
        elif len(numbers) == 1:
            axis, loc = re.search('([x-y])\=(\d+)', line).group(1,2)
            fold_instructions.append(( axis, int(loc) ))


paper = np.full((max_y+1, max_x+1), False)
for x, y in coor_set:
    paper[y][x] = True


for ins in fold_instructions:
    paper = fold(paper, ins)

output = ''
for line in paper:
    for val in line:
        if val:
            output += '#'
        else:
            output += '.'
    output += '\n'

print(output)
