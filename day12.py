from aoc_help import *
import timeit
import numpy as np

day = 12
get_input(day)
lines = read_file(f'data/input-day{day:02}.txt')
start_time = timeit.default_timer()

data = [(l.split('-')[0], l.split('-')[1]) for l in lines]


# part 1
def is_big(cave):
    if len(cave) > 1:
        return ord(cave[0]) < 91
    return ord(cave) < 91


data += [(x[1], x[0]) for x in data]
edges = {}
for edge in data:
    key, value = edge[0], edge[1]
    if key in edges.keys():
        edges[key] += [value]
    else:
        edges[key] = [value]

# filter paths
edges.pop('end')
for k, v in edges.items():
    if 'start' in v:
        v.remove('start')

paths = [['start', n] for n in edges['start']]
finals = []

while paths:
    remove_list = []
    add_list = []
    for p in paths:
        if 'end' in p:
            finals += [p]
            remove_list += [p]
        else:
            remove_list += [p]
            for el in edges[p[-1]]:
                if is_big(el) or el not in p:
                    new_p = p.copy() + [el]
                    add_list += [new_p]
    for e in remove_list:
        paths.remove(e)
    for e in add_list:
        paths += [e]

sol1 = len(finals)
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")


# part 2
def ok_to_add(path, el):
    if is_big(el):
        return True
    unique_elements = set(path)
    for ue in unique_elements:
        if is_big(ue) or ue == 'start' or ue == 'end':
            continue
        if path.count(ue) > 1:
            return el not in unique_elements
    return True


paths = [['start', n] for n in edges['start']]
finals = []

while paths:
    remove_list = []
    add_list = []
    for p in paths:
        if 'end' in p:
            finals += [p]
            remove_list += [p]
        else:
            remove_list += [p]
            for el in edges[p[-1]]:
                if ok_to_add(p, el):
                    new_p = p.copy() + [el]
                    add_list += [new_p]
    for e in remove_list:
        paths.remove(e)
    for e in add_list:
        paths += [e]

sol2 = len(finals)
part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {sol2} ({part2_time:.4f}s after part1)")
