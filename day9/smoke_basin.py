import sys
import numpy as np


def number_by_number(heights):
    low_points = []
    for i in range(len(heights)):
        for j in range(len(heights[i])):
            is_low_point = True
            if i != 0:
                if heights[i-1][j] <= heights[i][j]:
                    is_low_point &= False
            if i != len(heights)-1:
                if heights[i+1][j] <= heights[i][j]:
                    is_low_point &= False
            if j != 0:
                if heights[i][j-1] <= heights[i][j]:
                    is_low_point &= False
            if j != len(heights[i])-1:
                if heights[i][j+1] <= heights[i][j]:
                    is_low_point &= False
            if is_low_point:
                low_points.append((i,j))
    return low_points

def sum_points(heights, low_points):
    total = 0
    for point in low_points:
        total += heights[point[0]][point[1]] + 1
    return total


def find_basins(heights, low_points):
    visited = np.zeros((len(heights),len(heights[0])))
    basin_sizes = []
    for point in low_points:
        volume = fill_basin(point[0], point[1], heights, visited)
        basin_sizes.append(volume)
    return basin_sizes

def fill_basin(x, y, heights, visited):
    if x < 0 or y < 0 or x >= len(heights) or y >= len(heights[x]):
        return 0
    elif visited[x][y]:
        return 0
    elif heights[x][y] == 9:
        return 0

    visited[x][y] = 1
    volume = 0
    volume += fill_basin(x+1, y, heights, visited)
    volume += fill_basin(x-1, y, heights, visited)
    volume += fill_basin(x, y+1, heights, visited)
    volume += fill_basin(x, y-1, heights, visited)
    return volume + 1

with open(sys.argv[1], 'r') as in_file:
    vent_map = [list(map(int,list(line.rstrip()))) for line in in_file]


danger_points = number_by_number(vent_map)
sol = sum_points(vent_map, danger_points)

basin_sizes = find_basins(vent_map, danger_points)
basin_sizes.sort()
sol2 = np.prod(basin_sizes[-3:])
print(sol2)
