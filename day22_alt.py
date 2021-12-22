from collections import defaultdict
from collections import Counter
from aoc_help import *


lines = read_file(f'data/input-day22t.txt')

instructions = [x.split()[0] for x in lines]
coords = [x.split()[1] for x in lines]
x_ranges = [(int(x.split(',')[0].strip('x=').split('..')[0]), int(x.split(',')[0].strip('x=').split('..')[1])) for x in coords]
y_ranges = [(int(x.split(',')[1].strip('y=').split('..')[0]), int(x.split(',')[1].strip('y=').split('..')[1])) for x in coords]
z_ranges = [(int(x.split(',')[2].strip('z=').split('..')[0]), int(x.split(',')[2].strip('z=').split('..')[1])) for x in coords]
my_cubes = []
for i in range(len(instructions)):
    my_cubes += [x_ranges[i], y_ranges[i], z_ranges[i]]


cubes = []
for i in range(len(instructions)):
    [op, ux, vx, uy, vy, uz, vz] = instructions[i], x_ranges[i][0], x_ranges[i][1], y_ranges[i][0], y_ranges[i][1], z_ranges[i][0], z_ranges[i][1]
    for cubes_i in range(len(cubes)):
        [ux2, vx2, uy2, vy2, uz2, vz2] = cubes[cubes_i]
        if ux > vx2 or vx < ux2 or uy > vy2 or vy < uy2 or uz > vz2 or vz < uz2: # new on zone not overlapping existing on zone
            continue
        cubes[cubes_i] = None
        if ux > ux2:
            cubes.append((ux2, ux - 1, uy2, vy2, uz2, vz2))
        if vx < vx2:
            cubes.append((vx + 1, vx2, uy2, vy2, uz2, vz2))
        if uy > uy2:
            cubes.append((max(ux2, ux), min(vx2, vx), uy2, uy - 1, uz2, vz2))
        if vy < vy2:
            cubes.append((max(ux2, ux), min(vx2, vx), vy + 1, vy2, uz2, vz2))
        if uz > uz2:
            cubes.append((max(ux2, ux), min(vx2, vx), max(uy2, uy), min(vy2, vy), uz2, uz - 1))
        if vz < vz2:
            cubes.append((max(ux2, ux), min(vx2, vx), max(uy2, uy), min(vy2, vy), vz + 1, vz2))
    if op == 'on':
        cubes.append((min(ux, vx), max(ux, vx), min(uy, vy), max(uy, vy), min(uz, vz), max(uz, vz)))
    cubes = [cube for cube in cubes if cube is not None]
    print(cubes)

on_count = 0
for cube in cubes:
    [ux, vx, uy, vy, uz, vz] = cube
    on_count += (vx - ux + 1) * (vy - uy + 1) * (vz - uz + 1)
print(len(cubes))
print(cubes)
print(on_count)

