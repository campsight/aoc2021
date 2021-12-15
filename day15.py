from aoc_help import *
import timeit
import numpy as np

day = 15
get_input(day)
lines = read_file(f'data/input-day{day:02}.txt')
start_time = timeit.default_timer()

data1 = [[int(x) for x in y] for y in lines]


# part 1
def get_children(point, risk, grid, visited):
    x, y = point[0], point[1]
    children = []
    for (n, m) in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]:
        if (n >= 0) and (m >= 0) and (n < len(grid)) and (m < len(grid[0])) and (n,m) not in visited:
            children += [(risk + grid[n][m], (n, m))]
    return children


def insert_path(paths, point, risk):
    np = []
    added = False
    for i in range(len(paths)):
        cp = paths[i]
        if (not added) and risk <= cp[0]:
            np += [(risk, point)]
            added = True
        np += [cp]
    if not added:  # if not yet added, append it to the end
        np += [(risk, point)]
    return np


def my_dijkstra(data):
    paths = [(0, (0, 0))]
    visited = {(0, 0)}
    finished = False
    solution = 0
    endpoint = (len(data) - 1, len(data[0]) - 1)
    while not finished:
        p = paths.pop(0)
        p_risk, p_point = p[0], p[1]
        for child in get_children(p_point, p_risk, data, visited):
            new_risk, new_p = child[0], child[1]
            if new_p == endpoint:
                finished = True
                solution = new_risk
                break
            paths = insert_path(paths, new_p, new_risk)
            visited.add(new_p)
    return solution


sol1 = my_dijkstra(data1)
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")

# part 2
new_grid = np.tile(np.array(data1), (5, 5))

ro = len(data1)
co = len(data1[0])
for r in range(len(new_grid)):
    for c in range(len(new_grid[0])):
        add_r = r // ro
        add_c = c // co
        new_v = new_grid[r][c] + add_r + add_c
        if new_v > 9:
            new_v = new_v % 9
        new_grid[r][c] = new_v

sol2 = my_dijkstra(new_grid)
part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {sol2} ({part2_time:.4f}s after part1)")
