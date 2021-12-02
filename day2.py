from aoc_help import *
lines = read_file('data/input-day2.txt')
data = [x.split(" ") for x in lines]

FW = "forward"
D = "down"
U = "up"

# part 1
hpos = 0
depth = 0

for instr in data:
    cmd = instr[0]
    dist = int(instr[1])
    if cmd == FW:
        hpos += dist
    elif cmd == D:
        depth += dist
    elif cmd == U:
        depth -= dist

print(f"Part 1: hpos is {hpos} and depth is {depth} => solution = {depth*hpos}")

# part 2
hpos = 0
depth = 0
aim = 0

for instr in data:
    cmd = instr[0]
    dist = int(instr[1])
    if cmd == FW:
        hpos += dist
        depth += aim*dist
    elif cmd == D:
        aim += dist
    elif cmd == U:
        aim -= dist

print(f"Part 2: hpos is {hpos} and depth is {depth} and aim is {aim} => solution = {depth*hpos}")