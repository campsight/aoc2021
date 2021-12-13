from aoc_help import *
import timeit
import numpy as np

day = 13
get_input(day)
lines = read_file(f'data/input-day{day:02}.txt')
start_time = timeit.default_timer()

fold_instr = []

while True:
    l = lines[-1]
    if l and l[0] == 'f':
        axes, number = l.replace("fold along ", "").split('=')
        fold_instr += [(axes, int(number))]
        lines.remove(l)
    else:
        break
lines.remove(lines[-1])  # empty line between coordinates and fold instructions
dots = [(int(l.split(',')[0]), int(l.split(',')[1])) for l in lines]

# part 1
width = max([x[0] for x in dots])+1
length = max([x[1] for x in dots])+1
sheet = np.zeros((length, width), dtype=np.int8)
for d in dots:
    sheet[d[1], d[0]] = 1
fold_instr.reverse()


def exec_instr(instr, sheet, length, width):
    if instr[0] == 'y':  # fold up
        for i in range(instr[1]):
            for j in range(width):
                sheet[i, j] = max(sheet[i, j], sheet[(2*instr[1])-i, j])
        length = instr[1]
    else:  # fold right to left
        for j in range(instr[1]):
            for i in range(length):
                sheet[i, j] = max(sheet[i, j], sheet[i, (2*instr[1])-j])
        width = instr[1]
    sheet = sheet[0:length, 0:width]
    return sheet, length, width


sheet, length, width = exec_instr(fold_instr[0], sheet, length, width)
sol1 = np.sum(sheet)
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")

# part 2
for instr in fold_instr[1:len(fold_instr)]:
    sheet, length, width = exec_instr(instr, sheet, length, width)

symbols = np.array([' ', '*'])
print_sheet = symbols[sheet]
for line in print_sheet:
    print(''.join(line))

part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: read above :-) ({part2_time:.4f}s after part1)")
