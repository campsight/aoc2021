from aoc_help import *
import timeit
import math
import numpy as np

day = 18
get_input(day)
lines = read_file(f'data/input-day{day:02}.txt')
start_time = timeit.default_timer()


# part 1
def find_left(pos, line):
    for i in range(pos, -1, -1):
        if isinstance(line[i], int):
            return i
    return -1


def find_right(pos: int, line: str) -> int:
    for i in range(pos, len(line)):
        if isinstance(line[i], int):
            return i
    return -1


def get_number(pos, line):
    nls = ''
    while line[pos].isdigit():
        nls += line[pos]
        pos += 1
    return nls


def explode(line, pos):
    ell = line[pos+1]
    elr = line[pos+3]
    l = find_left(pos-1, line)
    if l > 0:
        line[l] += ell
    r = find_right(pos+5, line)
    if r > 0:
        line[r] += elr
    return line[:pos] + [0] + line[pos+5:]


def split(line, pos):
    nb = line[pos]
    left = math.floor(nb / 2)
    right = math.ceil(nb / 2)
    return line[:pos] + ["[", left, ",", right, "]"] + line[pos+1:]


def reduce_line(line):
    opens = 0
    for i, c in enumerate(line):
        if c == ']':
            opens -= 1
        elif c == '[':
            opens += 1
            if opens == 5:
                return True, explode(line, i)
    return False, line


def exec_split(line):
    for i, c in enumerate(line):
        if isinstance(c, int) and c >= 10:
            return True, split(line, i)
    return False, line


def process_line(line):
    cont = True
    l = line
    while cont:
        cont, l = reduce_line(l)
        # if cont:
          #   print(f"Reduction executed. New line = {''.join([str(e) for e in line])}")
        if not cont:
            cont, l = exec_split(l)
        #     if cont:
          #       print(f"Split executed. New line = {''.join([str(e) for e in line])}")
    return l


data = [[int(c) if c.isdigit() else c for c in line] for line in lines]

my_sum = data[0]
for i in range(1, len(data)):
    # if not a: return b
    my_sum = ['['] + my_sum + [','] + data[i] + [']']
    # print(''.join([str(e) for e in my_sum]))
    my_sum = process_line(my_sum)
    # print(''.join([str(e) for e in my_sum]))
    # print()


def find_pair(line):
    replace_list = []
    i = 0
    while i < (len(line)-3):
        c = line[i]
        if c not in (',', '[', ']'):
            end1 = i
            while line[end1].isdigit():
                end1 += 1
            if line[end1] == "," and line[end1+1].isdigit():
                end2 = end1+1
                while line[end2].isdigit():
                    end2 += 1
                n1 = int(line[i:end1])
                n2 = int(line[(end1+1):end2])
                # print(f"pair found at pos {i}: {n1}, {n2}")
                magnitude = n1*3 + n2*2
                replace_list += [(i-1, end2+1, str(magnitude))]
                i = end2+1
            else:
                i = end1
        else:
            i += 1
    prev = 0
    new_string = ''
    for i in range(len(replace_list)):
        repl = replace_list[i]
        new_string += line[prev:repl[0]]
        new_string += repl[2]
        prev = repl[1]
    new_string += line[replace_list[-1][1]:len(line)]
    # print(line)
    # print(replace_list)
    # print(new_string)
    return new_string


def calculate_magnitude(line):
    while len(line) > 1:
        for i in range(len(line)):
            if isinstance(line[i], int) and isinstance(line[i + 2], int):
                line = line[:i - 1] + [line[i] * 3 + line[i + 2] * 2] + line[i + 4:]
                break
    return line[0]


sol1 = calculate_magnitude(my_sum)
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")


# part 2
my_sum = data[0]
for i in range(1, len(data)):
    # if not a: return b
    my_sum = ['['] + my_sum + [','] + data[i] + [']']
    # print(''.join([str(e) for e in my_sum]))
    my_sum = process_line(my_sum)
    # print(''.join([str(e) for e in my_sum]))
    # print()

maxval = 0
for s1 in data:
    for s2 in data:
        if s1 == s2:
            continue
        val = calculate_magnitude(process_line(['['] + s1 + [','] + s2 + [']']))
        if val > maxval:
            maxval = val

sol2 = maxval
part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {sol2} ({part2_time:.4f}s after part1)")
