from aoc_help import *
import timeit
import numpy as np

get_input(9)
lines = read_file('data/input-day09t.txt')
start_time = timeit.default_timer()

# part 1

sol1 = 0
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")


# part 2

sol2 = 0
part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {sol2} ({part2_time:.4f}s after part1)")
