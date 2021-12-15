from aoc_help import *
import timeit
import numpy as np

day = 14
get_input(day)
lines = read_file(f'data/input-day{day:02}.txt')
start_time = timeit.default_timer()

polystart = lines[0]
lines.pop(0)
lines.pop(0)

inserts = {l.split(' -> ')[0]: l.split(' -> ')[1] for l in lines}


# part 1
def run_cycle(strain, inserts):
    to_insert = []
    for i in range(len(strain)-1):
        next_el = strain[i:i+2]
        repl = inserts.get(next_el, '')
        to_insert += [repl]
    to_insert += ['']
    new_strain = []
    for i in range(len(strain)):
        if to_insert[i] == '':
            new_strain += [strain[i]]
        else:
            new_strain += [strain[i], to_insert[i]]
    return ''.join(new_strain)


strain = polystart
for i in range(10):
    strain = run_cycle(strain, inserts)

all_letters = [e[0] for e in inserts.keys()]
all_letters += [e[1] for e in inserts.keys()]
ocs = {}
for el in set(all_letters):
    ocs[el] = strain.count(el)

sol1 = max(ocs.values()) - min(ocs.values())
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")


# part 2
def run_cycle2(pairs, inserts):
    result = {}
    for p, n in pairs.items():
        new_el = inserts.get(p, '')
        if new_el != '':
            pair1 = ''.join([p[0], new_el])
            pair2 = ''.join([new_el, p[1]])
            result[pair1] = result.get(pair1, 0) + n
            result[pair2] = result.get(pair2, 0) + n
    return result


start = {}
for i in range(len(polystart)-1):
    pair = ''.join([polystart[i], polystart[i+1]])
    start[pair] = start.get(pair, 0) + 1

next_strain = start
for i in range(40):
    next_strain = run_cycle2(next_strain, inserts)

ocs = {e:0 for e in set(all_letters)}
for pair, n in next_strain.items():
    ocs[pair[0]] = ocs.get(pair[0], 0) + n
    ocs[pair[1]] = ocs.get(pair[1], 0) + n

for pair in ocs:
    ocs[pair] = ocs[pair] // 2
ocs[polystart[0]] += 1
ocs[polystart[-1]] += 1
print(max(ocs.values()))
sol2 = max(ocs.values()) - min(ocs.values())
part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {sol2} ({part2_time:.4f}s after part1)")
