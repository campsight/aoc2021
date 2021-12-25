import copy

from aoc_help import *
import timeit
import numpy as np

day = 25
get_input(day)
lines = read_file(f'data/input-day{day:02}.txt')
start_time = timeit.default_timer()

R = '>'
D = 'v'
EMPTY = '.'

grid = []
for i in range(len(lines)):
    grid += [[x for x in lines[i]]]

width = len(grid)


# part 1
def get_adjascent(r, c, grid):
    el = grid[r][c]
    if el == EMPTY:
        return False, -1,-1
    if el == R:
        nr = r
        nc = c+1 if c < len(grid[0])-1 else 0
        return True, nr, nc
    if el == D:
        nr = r+1 if r < len(grid)-1 else 0
        nc = c
        return True, nr, nc


def move_adjacent(r, c, grid):
    res, nr, nc = get_adjascent(r, c, grid)
    if res and grid[nr][nc] == EMPTY:
        return True, nr, nc
    return False, -1, -1


def execute_moves(move_list, grid, el):
    new_grid = copy.deepcopy(grid)
    for from_coord, to_coord in move_list:
        fr, fc, tr, tc = from_coord[0], from_coord[1], to_coord[0], to_coord[1]
        new_grid[fr][fc] = EMPTY
        new_grid[tr][tc] = el
    return new_grid


def do_cycle(grid):
    finished_right = False
    right_moves = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == R:
                res, to_r, to_c = move_adjacent(r, c, grid)
                if res:
                    right_moves += [((r, c), (to_r, to_c))]
    grid = execute_moves(right_moves, grid, R)
    if not right_moves: finished_right = True

    finished_down = False
    down_moves = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == D:
                res, to_r, to_c = move_adjacent(r, c, grid)
                if res:
                    down_moves += [((r, c), (to_r, to_c))]
    grid = execute_moves(down_moves, grid, D)
    if not down_moves: finished_down = True
    return (finished_down and finished_right), grid


def print_grid(grid):
    for g in grid:
        print("".join(g))
    print()


finished = False
step = 1
while not finished:
    print(step)
    finished, grid = do_cycle(grid)
    #print_grid(grid)
    step += 1


sol1 = step - 1
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")


# part 2

sol2 = 0
part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {sol2} ({part2_time:.4f}s after part1)")
