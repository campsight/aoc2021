from aoc_help import *
import timeit

get_input(8)
lines = read_file('data/input-day08.txt')
start_time = timeit.default_timer()

data = [(x.split('|')[0], x.split('|')[1]) for x in lines]
digits = [x[0].split() for x in data]
output = [x[1].split() for x in data]

# part 1
total = 0
for o in output:
    for d in o:
        total += len(d) in (2,3,4,7)
sol1 = total
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")


# part 2
def determine_digits(digin):
    result = ['a']*10
    d2 = [x for x in digin if len(x) == 2]
    d3 = [x for x in digin if len(x) == 3]
    d4 = [x for x in digin if len(x) == 4]
    d5 = [x for x in digin if len(x) == 5]
    d6 = [x for x in digin if len(x) == 6]
    d7 = [x for x in digin if len(x) == 7]
    result[1] = d2[0]
    result[7] = d3[0]
    result[4] = d4[0]
    result[8] = d7[0]
    lowleft = [c for c in result[8] if c not in result[4] and c not in result[7]]
    for d in d6:
        not_lowleft = [c for c in d if c not in lowleft]
        not_right = [c for c in d if c not in result[1]]
        if len(not_lowleft) == 5:
            result[9] = d
        elif len(not_right) == 5:
            result[6] = d
        else:
            result[0] = d
    for d in d5:
        not_four = [c for c in d if c not in result[4]]
        not_one = [c for c in d if c not in result[1]]
        if len(not_four) == 3:
            result[2] = d
        elif len(not_one) == 3:
            result[3] = d
        else:
            result[5] = d
    return result


def get_digit(digits, digit):
    for i in range(len(digits)):
        if sorted(digits[i]) == sorted(digit):
            return i
    return -1


total = 0
for i in range(len(digits)):
    di = determine_digits(digits[i])
    total += sum([get_digit(di, output[i][j])*(10**(3-j)) for j in range(4)])

sol2 = total
part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {sol2} ({part2_time:.4f}s after part1)")
