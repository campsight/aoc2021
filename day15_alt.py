from aoc_help import *
import timeit
import numpy as np
from heapq import heappop, heappush

day = 15
get_input(day)
lines = read_file(f'data/input-day{day:02}.txt')
start_time = timeit.default_timer()

data = [[int(x) for x in y] for y in lines]


# part 1
def shortest_distance(my_data):
    rows = len(my_data)
    cols = len(my_data[0])
    heap = [(0, 0, 0)]
    visited = {(0, 0)}
    while heap:
        distance, x, y = heappop(heap)
        if x == rows - 1 and y == cols - 1:
            return distance

        for (n, m) in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]:
            if (n >= 0) and (m >= 0) and (n < rows) and (m < cols) and (n, m) not in visited:
                visited.add((n, m))
                heappush(heap, (distance + my_data[n][m], n, m))


sol1 = shortest_distance(data)
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")

# part 2

new_grid = np.tile(np.array(data), (5, 5))

ro = len(data)
co = len(data[0])
for r in range(len(new_grid)):
    for c in range(len(new_grid[0])):
        add_r = r // ro
        add_c = c // co
        new_v = new_grid[r][c] + add_r + add_c
        if new_v > 9:
            new_v = new_v % 9
        new_grid[r][c] = new_v

sol2 = shortest_distance(new_grid)
part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {sol2} ({part2_time:.4f}s after part1)")
