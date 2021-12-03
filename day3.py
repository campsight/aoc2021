from aoc_help import *
lines = read_file('data/input-day3.txt')

# part 1
gammas = [0]*len(lines[0])
nb_lines = len(lines)

for i in range(len(gammas)):
    gammas[i] = [x[i] for x in lines]

zeros = [g.count('0') for g in gammas]
ones = [g.count('1') for g in gammas]
gamma = [0]*len(gammas)

for i in range(len(gammas)):
    gamma[i] = '1' if zeros[i] < ones[i] else '0'

epsilon = [str(1-int(g)) for g in gamma]

numg = bin_to_int(gamma)
nume = bin_to_int(epsilon)

print(f"Solution part 1: gamma {numg} times epsilon {nume} = {numg*nume}")

# part 2
filterlist_oxygen = lines.copy()
filterlist_co2 = lines.copy()
for g in range(len(gamma)):
    if len(filterlist_oxygen) > 1:
        zeros_o = [x[g] for x in filterlist_oxygen].count('0')
        ones_o = len(filterlist_oxygen) - zeros_o
        mcv_o = 1 if ones_o >= zeros_o else 0
        filterlist_oxygen = [x for x in filterlist_oxygen if x[g] == str(mcv_o)]

    if len(filterlist_co2) > 1:
        zeros_c = [x[g] for x in filterlist_co2].count('0')
        ones_c = len(filterlist_co2) - zeros_c
        mcv_c = 1 if zeros_c > ones_c else 0
        filterlist_co2 = [x for x in filterlist_co2 if x[g] == str(mcv_c)]

numo = bin_to_int(filterlist_oxygen)
numc = bin_to_int(filterlist_co2)

print(f"Solution part 2: oxygen {numo} times co2 {numc} = {numo*numc}")
