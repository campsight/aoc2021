from aoc_help import *
import timeit
#import numpy as np

lines = read_file('data/input-day6.txt')
start_time = timeit.default_timer()

data = [int(x) for x in lines[0].split(',')]


# part 1
def run_cycle(fish):
    new_fish = {}
    for f, number in fish.items():
        new_fish[(f - 1)] = number
    nb_new = new_fish.pop(-1, 0)
    new_fish[6] = new_fish.get(6, 0) + nb_new
    new_fish[8] = nb_new
    return new_fish


fish = {x: data.count(x) for x in data}
for i in range(80):
    fish = run_cycle(fish)

sol1 = sum(fish.values())
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")

# part 2
for i in range(80, 256):
    fish = run_cycle(fish)

sol2 = sum(fish.values())
part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {sol2} ({part2_time:.4f}s after part1)")
