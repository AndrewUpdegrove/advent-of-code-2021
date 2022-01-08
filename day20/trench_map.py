import sys

def pad_image(grid, char):
    grid.insert(0, [char] * len(grid[0]))
    grid.append([char] * len(grid[0]))
    for i in range(len(grid)):
        grid[i].insert(0, char)
        grid[i].append(char)

def step_image(grid, algo, bonus_char):
    new_grid = [['$'] * len(line) for line in grid]
    pixel_map = {'#': '1', '.': '0'}
    for i, line in enumerate(grid):
        for j, char in enumerate(grid):
            bit_list = [(i+op1, j+op2) for op1 in range(-1,2) for op2 in range(-1,2)]
            bit_str = ''
            for p in bit_list:
                if p[0] in range(len(grid)) and p[1] in range(len(line)):
                    bit_str += pixel_map[grid[p[0]][p[1]]]
                else:
                    bit_str += pixel_map[bonus_char]
            bin_num = int(bit_str, 2)
            new_grid[i][j] = algo[bin_num]

    return new_grid
            
def solve_1(grid, algo):
    pad_image(grid, '.')
    grid = step_image(grid, algo, '.')
    pad_image(grid, '#')
    grid = step_image(grid, algo, '#')
    light_sum = 0
    for line in grid:
        light_sum += line.count('#')
    return light_sum

def solve_2(grid, algo):
    for i in range(50):
        if i % 2 ==1: print(f'Performing expansion {i+1}')
        all_other_char = '.' if i % 2 == 0 else '#'
        pad_image(grid, all_other_char)
        grid = step_image(grid, algo, all_other_char)
    light_sum = 0
    for line in grid:
        light_sum += line.count('#')
    return light_sum


with open(sys.argv[1], 'r') as f:
    enhance_algo = f.readline().rstrip()
    _ = f.readline()
    pic_grid = [ list(l.rstrip()) for l in f]

# print(solve_1(pic_grid, enhance_algo))
print(solve_2(pic_grid, enhance_algo))

