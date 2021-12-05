from aoc_help import *
import timeit

lines = read_file('data/input-day5.txt')

start_time = timeit.default_timer()

# part 1
data = [x.split(' -> ') for x in lines]
from_c = [(int(x[0].split(',')[0]), int(x[0].split(',')[1]))  for x in data]
to_c = [(int(x[1].split(',')[0]), int(x[1].split(',')[1]))  for x in data]
lines = []
max_x = 0
max_y = 0
for i in range(len(from_c)):
    f = from_c[i]
    t = to_c[i]
    if (f[0] == t[0]) or (f[1] == t[1]):
        lines += [(f, t)]
        if f[0] > max_x:
            max_x = f[0]
        if t[0] > max_x:
            max_x = t[0]
        if f[1] > max_y:
            max_y = f[1]
        if t[1] > max_y:
            max_y = t[1]

# print(lines)
# print([max_x, max_y])


def add_line(line, grid):
    # vertical line: x1 == x2
    x1 = line[0][0]
    y1 = line[0][1]
    x2 = line[1][0]
    y2 = line[1][1]
    if x1 == x2:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for i in range(y1, (y2+1)):
            grid[x1][i] += 1
    elif y1 == y2: # horizontal line
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for i in range(x1, (x2+1)):
            grid[i][y1] += 1
    else: # exactly 45 degrees
        if (x2 > x1) and (y2 > y1):
            for i in range(0, (x2-x1+1)):
                grid[x1+i][y1+i] += 1
        elif (x2 > x1) and (y2 < y1):
            for i in range(0, (x2-x1+1)):
                grid[x1+i][y1-i] += 1
        elif (x1 > x2) and (y2 > y1):
            for i in range(0, (x1-x2+1)):
                grid[x2+i][y2-i] += 1
        elif (x1 > x2) and (y2 < y1):
            for i in range(0, (x1-x2+1)):
                grid[x2+i][y2+i] += 1


my_grid = [[0 for r in range(max_y+1)] for c in range(max_x+1)]
for l in lines:
    add_line(l, my_grid)

intersects = 0
for r in range(max_x + 1):
    for c in range(max_y + 1):
        if my_grid[r][c] > 1:
            intersects += 1

part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {intersects} (after {part1_time:.4f}s)")

# part 2
lines = []
max_x = 0
max_y = 0
for i in range(len(from_c)):
    f = from_c[i]
    t = to_c[i]
    lines += [(f, t)]
    if f[0] > max_x:
        max_x = f[0]
    if t[0] > max_x:
        max_x = t[0]
    if f[1] > max_y:
        max_y = f[1]
    if t[1] > max_y:
        max_y = t[1]


my_grid = [[0 for r in range(max_y+1)] for c in range(max_x+1)]
for l in lines:
    add_line(l, my_grid)

intersects = 0
for r in range(max_x + 1):
    for c in range(max_y + 1):
        if my_grid[r][c] > 1:
            intersects += 1

part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {intersects}, ({part2_time:.4f}s after part1)")
