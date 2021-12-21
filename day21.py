import copy
from itertools import *
from collections import defaultdict
from aoc_help import *
import timeit

day = 21
get_input(day)
lines = read_file(f'data/input-day{day:02}t.txt')
start_time = timeit.default_timer()

P1, P2 = 6, 8  # 3, 7 for the example. One less than stated as I use 0..9 for the positions instead of 1..10


# part 1
def my_dice(max_nb):
    n = 0
    while True:
        n = (n % max_nb) + 1
        yield n


def sum_roll(dice, nb):
    s = 0
    for i in range(nb):
        s += next(dice)
    return s


p1, s1, p2, s2 = P1, 0, P2, 0
dice = my_dice(100)
nb_rolls = 0
while (s1 < 1000) and (s2 < 1000):
    d = sum_roll(dice, 3)
    nb_rolls += 3
    p1 = (p1+d) % 10
    s1 += p1 + 1
    if s1 < 1000:
        d = sum_roll(dice, 3)
        nb_rolls += 3
        p2 = (p2 + d) % 10
        s2 += p2 + 1

sol1 = min(s1, s2) * nb_rolls
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")

# part 2
quantum_dice = (1, 2, 3)
quantum_sums = defaultdict(int)
for subset in product(quantum_dice, repeat=3):
    quantum_sums[sum(subset)] += 1


def run_quantum_turn(game_state, p1_wins, p2_wins):
    p1, s1, p2, s2 = game_state
    turn_set = defaultdict(int)
    for d, times in quantum_sums.items():
        np1 = (p1 + d) % 10
        ns1 = s1 + np1 + 1
        if ns1 >= 21:
            p1_wins += nb * times
            continue
        for d2, times2 in quantum_sums.items():
            np2 = (p2 + d2) % 10
            ns2 = s2 + np2 + 1
            if ns2 >= 21:
                p2_wins += nb * times * times2
                continue
            turn_set[(np1, ns1, np2, ns2)] += nb * times * times2
    return p1_wins, p2_wins, turn_set


def merge_defaultdicts(d1, d2):
    if not d2:
        return d1
    for k, v in d2.items():
        d1[k] += v
    return d1


p1_wins, p2_wins = 0, 0
all_sets = {(P1, 0, P2, 0): 1}
while all_sets:
    next_set = defaultdict(int)
    for el, nb in all_sets.items():
        p1_wins, p2_wins, quantum_set = run_quantum_turn(el, p1_wins, p2_wins)
        next_set = merge_defaultdicts(next_set, quantum_set)
    all_sets = next_set

sol2 = max(p1_wins, p2_wins)
part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {sol2} ({part2_time:.4f}s after part1)")
