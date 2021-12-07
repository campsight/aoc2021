from aoc_help import *
import timeit
import numpy as np

lines = read_file('data/input-day7.txt')
start_time = timeit.default_timer()

data = [int(x) for x in lines[0].split(',')]

# part 1
med = int(np.median(data))
sol1 = sum([abs(c - med) for c in data])
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")


# part 2
def i_sum(n):
    return n * (n+1) / 2


mini, maxi = min(data), (max(data)+1)
lowest = 9999999999
for i in range(mini, maxi):
    fuel_sum = sum([i_sum(abs(c - i)) for c in data])
    if fuel_sum < lowest:
        lowest = fuel_sum

sol2 = int(lowest)
part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {sol2} ({part2_time:.4f}s after part1)")

# day 15 2020 input 9,12,1,4,17,0,18