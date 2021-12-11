from aoc_help import *
import timeit
import numpy as np

day = 11
get_input(day)
lines = read_file(f'data/input-day{day:02}.txt')
start_time = timeit.default_timer()

data = [[int(x) for x in y] for y in lines]


# part 1
def flash(data, flashed):
    el_flashed = False
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == 10 and (r, c) not in flashed:
                for m in range(r - 1, r + 2):
                    for n in range(c - 1, c + 2):
                        if not (m == r and n == c) \
                                and n > -1 and m > -1 \
                                and n < len(data) and m < len(data[0]) \
                                and data[m][n] < 10:
                            data[m][n] += 1
                flashed += [(r, c)]
                el_flashed = True
    if el_flashed:
        return flash(data, flashed)
    else:
        return len(flashed)


def run_cycle(data):
    # increase all with 1
    for r in range(len(data)):
        for c in range(len(data[0])):
            data[r][c] += 1
    # flash tens
    nb_flashes = flash(data, [])
    # set 10s to 0
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == 10:
                data[r][c] = 0
    return nb_flashes


total = 0
for i in range(100):
    total += run_cycle(data)

sol1 = total
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")

# part 2
found = False
i = 101
while not found:
    run_cycle(data)
    found = max(max(data)) == 0
    i += 1

sol2 = i - 1
part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {sol2} ({part2_time:.4f}s after part1)")
