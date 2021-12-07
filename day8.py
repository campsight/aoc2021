from aoc_help import *
import timeit
import numpy as np

lines = read_file('data/input-day8t.txt')
start_time = timeit.default_timer()

data = [int(x) for x in lines[0].split(',')]

# part 1

sol1 = 0
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")


# part 2
sol2 = 0
part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {sol2} ({part2_time:.4f}s after part1)")

# day 15 2020 input 9,12,1,4,17,0,18