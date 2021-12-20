import copy

from aoc_help import *
import timeit
import numpy as np

day = 20
get_input(day)
lines = read_file(f'data/input-day{day:02}t.txt')
start_time = timeit.default_timer()

CONV = [".", "#"]

algo = [CONV.index(x) for x in lines[0]]

grid = []
for i in range(2, len(lines)):
    grid += [[CONV.index(x) for x in lines[i]]]


# part 1
def calculate_pixel(r, c, cgrid):
    result = []
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if r == 0 or c == 0 or r == len(cgrid) or c == len(cgrid[0]):
                result += [0]
            else:
                result += [cgrid[r+dr][c+dc]]
    result_str = [str(x) for x in result]
    index = bin_to_int("".join(result_str))
    return algo[index]


def enhance_image(grid, ext):
    # print(f"grid of size {len(grid)} * {len(grid[0])}")
    egrid = extend_grid(grid, ext)
    egrid = extend_grid(egrid, ext)
    egrid = extend_grid(egrid, ext)
    result = copy.deepcopy(egrid)
    for r in range(1, len(egrid) - 1):
        for c in range(1, len(egrid[0]) - 1):
            result[r][c] = calculate_pixel(r, c, egrid)
    return get_subgrid(result), 1-ext


my_grid = copy.deepcopy(grid)
ext = 0
for i in range(2):
    my_grid, ext = enhance_image(my_grid, ext)

sol1 = grid_values(my_grid, 1)
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")

# part 2
for i in range(48):
    my_grid, ext = enhance_image(my_grid, ext)

sol2 = grid_values(my_grid, 1)
part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {sol2} ({part2_time:.4f}s after part1)")
