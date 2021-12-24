import copy

from aoc_help import *
import timeit

day = 24
get_input(day)
lines = read_file(f'data/input-day{day:02}.txt')
start_time = timeit.default_timer()

ADD_X = [14, 15, 12, 11, -5, 14, 15, -13, -16, -8, 15, -8, 0, -4]
ADD_Y = [12, 7, 1, 2, 4, 15, 11, 5, 3, 9, 2, 3, 3, 11]
MOD_Z = [1, 1, 1, 1, 26, 1, 1, 26, 26, 26, 1, 26, 26, 26]


# part 1
# original code to run the program fully. Much too slow, but I leave it in for reference
def run_prog(instructions, model_number, values):
    pointer = 0
    prog_inp = str(model_number)
    for instr in instructions:
        instr_set = instr.split()
        op = instr_set[0]
        arg1 = instr_set[1]
        arg2 = '0' if len(instr_set) == 2 else instr_set[2]
        if op == "inp":
            values[arg1] = int(prog_inp[pointer])
            pointer += 1
        else:
            if arg2.lstrip('-+').isdigit():
                value2 = int(arg2)
            else:
                value2 = values[arg2]
            if op == "add":
                values[arg1] += value2
            elif op == "mul":
                values[arg1] *= value2
            elif op == "div":
                values[arg1] = values[arg1] // value2
            elif op == "mod":
                values[arg1] = values[arg1] % value2
            elif op == "eql":
                values[arg1] = 1 if values[arg1] == value2 else 0
    return values


# Second part: how I came to the final part (so also this part is not used)
# Analyzing the input code input by input ('inp w' as separator)
# Then detecting a pattern => going to the final solution
def run_part_prog(model_number):
    inp = str(model_number)
    values = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    # part 1: x = 1, y = 12 + d0, z = y
    digit_0 = int(inp[0])
    values['w'] = digit_0
    values['x'] = 1
    values['y'] = digit_0 + 12
    values['z'] = values['y']

    # part 2: w becomes second digit, x = 1, y = 7 + d1, z = 26 * (12+d0) + y
    digit_1 = int(inp[1])
    values['w'] = digit_1
    values['y'] = 7 + digit_1
    values['z'] = 26 * values['z'] + values['y']

    # part 3: w becomes third digit, x = 1, y = 7 + d2, z = 26*z + y
    digit_2 = int(inp[2])
    values['w'] = digit_2
    values['y'] = 1 + digit_2
    values['z'] = 26 * values['z'] + values['y']

    return values


# final code running one cycle. Every input cycle is the same in code, but uses other
# numbers to be added to x and y and z is sometimes modulo 26, sometimes modulo 1
def run_cycle(pos, current_w, current_z):
    x = ADD_X[pos] + (current_z % 26)
    z = current_z // MOD_Z[pos]
    if x != current_w:  # eql x w => x becomes 1 or zero; if it is 1 multiplications have an effect, else not
        z *= 26
        z += current_w + ADD_Y[pos]
    return z


# MAX Z to stop searching in time. As z is inputs multiplied by 26 and afterwords modulo 26, the maximum
# number is 26**n where n is the number of modulo 26 operations still remaining in next steps
MAX_Z = [26 ** len([x for x in range(14) if MOD_Z[x] == 26 and x >= i]) for i in range(14)]


# Part of the initial brute force attempt => can be ignored
# for model_number in range(99999999999999, -1, -1):
#    snm = str(model_number)
#    if '0' in snm:
#        continue
# print(f"Testing model number: {model_number}")
#    test = run_prog(lines, model_number)
#    if test['z'] == 0:
#        print(f"Valid model number found: {model_number}")
#        break
DIGITS = list(range(1,10))


def search_solutions(pos, z):
    if pos == 14:
        if z == 0:
            #print(f"Solution found :-)")
            return [""]
        else:
            return []
    if z > MAX_Z[pos]:
        return []
    next_x = z % 26 + ADD_X[pos]
    possible_ws = [next_x] if next_x in DIGITS else DIGITS  # try all possibilities, except if the next_x is a digit because of the "eql x w" statement. This can only be true if x is a digit below 10
    result = []
    for w in possible_ws:
        sols = search_solutions(pos + 1, run_cycle(pos, w, z))
        for s in sols:
            result += [str(w) + s]
    return result


all_solutions = search_solutions(0, 0)
all_solution_nbs = [int(x) for x in all_solutions]
print("num solutions", len(all_solutions))

sol1 = max(all_solution_nbs)
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")


# part 2
sol2 = min(all_solution_nbs)
part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {sol2} ({part2_time:.4f}s after part1)")