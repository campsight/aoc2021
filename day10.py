from aoc_help import *
import timeit
import numpy as np

day = 10
get_input(day)
lines = read_file(f'data/input-day{day:02}.txt')
start_time = timeit.default_timer()

CORRUPT, INCOMPLETE = -1, 0
openings = ["(", "[", "{", "<"]
closings = [")", "]", "}", ">"]
points = {")": 3,
          "]": 57,
          "}": 1197,
          ">": 25137}


# part 1
def get_result(line):
    opens = []
    closes = []
    for c in line:
        if c in openings:
            opens += [c]
            closes += closings[openings.index(c)]
        elif c in closings:
            if closes and (closes[-1] == c):
                closes.pop()
                opens.pop()
            else:
                return CORRUPT, c
        else:
            print(f"illegal char {c} in {line}")
    return INCOMPLETE, closes


occs = {k:0 for k in points.keys()}
for l in lines:
    res, c = get_result(l)
    if res == CORRUPT:
        occs[c] += 1

total = 0
for c, n in occs.items():
    total += points[c] * n

sol1 = total
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")


# part 2
def calculate_score(closers):
    closers.reverse()
    result = 0
    for c in closers:
        result *= 5
        result += closings.index(c) + 1
    return result


scores = []
for l in lines:
    res, missings = get_result(l)
    if res == INCOMPLETE:
        score = calculate_score(missings)
        scores += [score]

sol2 = sorted(scores)[len(scores)//2]
part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {sol2} ({part2_time:.4f}s after part1)")
