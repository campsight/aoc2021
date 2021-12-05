from aoc_help import *
import timeit

lines = read_file('data/input-day5.txt')

start_time = timeit.default_timer()

# part 1
data = [x.split(' -> ') for x in lines]
from_c = [(int(x[0].split(',')[0]), int(x[0].split(',')[1]))  for x in data]
to_c = [(int(x[1].split(',')[0]), int(x[1].split(',')[1]))  for x in data]
all_lines = [(from_c[i], to_c[i]) for i in range(len(from_c))]
hvlines = [l for l in all_lines if (l[0][0] == l[1][0]) or (l[0][1] == l[1][1])]
size = max(max([max(from_c), max(to_c)]))

my_grid = [[0 for r in range(size+1)] for c in range(size+1)]
for l in hvlines:
    add_line(l, my_grid)

intersects = 0
for r in range(size + 1):
    for c in range(size + 1):
        if my_grid[r][c] > 1:
            intersects += 1

part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {intersects} (after {part1_time:.4f}s)")

# part 2
my_grid = [[0 for r in range(size+1)] for c in range(size+1)]
for l in all_lines:
    add_line(l, my_grid)

intersects = 0
for r in range(size + 1):
    for c in range(size + 1):
        if my_grid[r][c] > 1:
            intersects += 1

part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {intersects} ({part2_time:.4f}s after part1)")
