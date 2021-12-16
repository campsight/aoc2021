import sys
from aoc_help import *
import timeit

day = 16
get_input(day)
lines = read_file(f'data/input-day{day:02}.txt')
start_time = timeit.default_timer()

data = lines[0]
bin_str = ''
for h in data:
    bin_str += (bin(int(h, 16))[2:]).zfill(4)


# part 1
def parse_literal(string, pos):
    nb_str = ''
    while True:
        next_bits = string[pos:(pos+5)]
        nb_str += next_bits[1:]
        if next_bits[0] == '0':
            return pos+5, int('0b' + nb_str, 2)
        pos += 5


def parse_len_op(string, pos, length):
    end = pos + length
    p = pos
    while p < end:
        p, n = parse_literal(string, p)
    return p


def instr_len(string, pos, len_ind):
    if len_ind == '0':
        subpacket_len = int('0b' + str(string[(pos + 1):(pos + 16)]), 2)
        startpos = pos + 16
        end = startpos + subpacket_len
        return startpos, end, True
    else:
        subpacket_nb = int('0b' + str(string[(pos + 1):(pos + 12)]), 2)
        startpos = pos + 12
        end = subpacket_nb
        return startpos, end, False


def parse_package(string, pos, ver):
    # print(f'Parse package at pos {pos}')
    versionb, typeb = string[pos:(pos+3)], string[(pos+3):(pos+6)]
    version = int('0b' + str(versionb), 2)
    type = int('0b' + str(typeb), 2)
    pos += 6
    if type == 4:
        p, n = parse_literal(string, pos)
        #print(f'Literal: {n}, continue at {p}')
        return p, n, ver + version
    else:
        len_ind = string[pos]
        v = version + ver

        if len_ind == '0':
            subpacket_len = int('0b' + str(string[(pos+1):(pos+16)]), 2)
            p = pos + 16
            end = p + subpacket_len
            i = 0
            while i < 1:
                p, n, v = parse_package(string, p, v)
                if p >= end:
                    i = 9999999
            return p, n, v
        else:
            subpacket_nb = int('0b' + str(string[(pos+1):(pos+12)]), 2)
            p = pos + 12
            i = 0
            while i < subpacket_nb:
                p, n, v = parse_package(string, p, v)
                i += 1
            return p, n, v


p, n, v = parse_package(bin_str, 0, 0)
sol1 = v
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")


# part 2
def parse_package2(string, pos):
    type = int('0b' + str(string[(pos+3):(pos+6)]), 2)
    # print(f"Parse package at pos {pos} type {type}")
    pos += 6
    if type == 4:
        p, n = parse_literal(string, pos)
        # print(f'Literal: {n}, continue at {p}')
        return p, n
    elif type in (0, 1, 2, 3):
        result = 0 if type in (0, 3) else 1
        if type == 2:
            result = sys.maxsize
        len_ind = string[pos]
        start, stop, endposcase = instr_len(string, pos, len_ind)
        i = 0
        p = start
        while i < stop:
            p, n = parse_package2(string, p)
            if type == 0:  # sum
                result += n
            elif type == 1:  # product
                result *= n
            elif type == 2:  # minimum
                result = min(result, n)
            elif type == 3:  # maximum
                result = max(result, n)
            if endposcase and p >= stop:
                i = stop
            if not endposcase:
                i += 1
        return p, result
    elif type in (5, 6, 7):
        len_ind = string[pos]
        start, stop, endposcase = instr_len(string, pos, len_ind)
        p = start
        p, n1 = parse_package2(string, p)
        p, n2 = parse_package2(string, p)
        if type == 5:
            return (p, 1) if n1 > n2 else (p, 0)
        if type == 6:
            return (p, 1) if n1 < n2 else (p, 0)
        if type == 7:
            return (p, 1) if n1 == n2 else (p, 0)


p, n = parse_package2(bin_str, 0)
sol2 = n
part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {sol2} ({part2_time:.4f}s after part1)")
