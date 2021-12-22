from aoc_help import *
import timeit

day = 22
get_input(day)
lines = read_file(f'data/input-day{day:02}.txt')
start_time = timeit.default_timer()

INSTR = ['off', 'on']
instructions = [INSTR.index(x.split()[0]) for x in lines]
coords = [x.split()[1] for x in lines]
x_ranges = [(int(x.split(',')[0].strip('x=').split('..')[0]), int(x.split(',')[0].strip('x=').split('..')[1])) for x in coords]
y_ranges = [(int(x.split(',')[1].strip('y=').split('..')[0]), int(x.split(',')[1].strip('y=').split('..')[1])) for x in coords]
z_ranges = [(int(x.split(',')[2].strip('z=').split('..')[0]), int(x.split(',')[2].strip('z=').split('..')[1])) for x in coords]
cubes = []
for i in range(len(instructions)):
    cubes += [(x_ranges[i], y_ranges[i], z_ranges[i])]


# part 1
def get_points(x1, x2, y1, y2, z1, z2, max):
    result = []
    for dx in range((x2-x1)+1):
        for dy in range((y2-y1)+1):
            for dz in range((z2-z1)+1):
                nx = x1+dx
                ny = y1+dy
                nz = z1+dz
                if (-max <= nx <= max) and (-max <= ny <= max) and (-max <= nz <= max):
                    result += [(nx, ny, nz)]
    return result


on_points = set()
for i in range(len(instructions)):
    instr = instructions[i]
    all_ranges = [*x_ranges[i], *y_ranges[i], *z_ranges[i]]
    if min(all_ranges) >= -50 and max(all_ranges) <= 50:
        points = get_points(*x_ranges[i], *y_ranges[i], *z_ranges[i], 50)
        if instr:
            on_points = on_points.union(points)
        else:
            on_points = on_points.difference(points)
sol1 = len(on_points)
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")


# part 2
def new_cubes(cube1, cube2):
    result = []
    x11, x12, y11, y12, z11, z12 = cube1[0][0], cube1[0][1], cube1[1][0], cube1[1][1], cube1[2][0], cube1[2][1]
    x21, x22, y21, y22, z21, z22 = cube2[0][0], cube2[0][1], cube2[1][0], cube2[1][1], cube2[2][0], cube2[2][1]
    if x11 > x22 or x12 < x21 or y11 > y22 or y12 < y21 or z11 > z22 or z12 < z21:  # new on zone not overlapping existing on zone
        return False, []
    if x21 < x11:
        result.append(((x21, x11-1), (y21, y22), (z21, z22)))
    if x22 > x12:
        result.append(((x12+1, x22), (y21, y22), (z21, z22)))
    if y21 < y11:
        result.append(((max(x11, x21), min(x12, x22)), (y21, y11-1), (z21, z22)))
    if y22 > y12:
        result.append(((max(x11, x21), min(x12, x22)), (y12+1, y22), (z21, z22)))
    if z21 < z11:
        result.append(((max(x11, x21), min(x12, x22)), (max(y11, y21), min(y12, y22)), (z21, z11-1)))
    if z22 > z12:
        result.append(((max(x11, x21), min(x12, x22)), (max(y11, y21), min(y12, y22)), (z12+1, z22)))
    return True, result


final_cubes = []
for i in range(len(instructions)):
    cube = cubes[i]
    remove_list = []
    append_list = []
    for other_cube in final_cubes:
        r, nc = new_cubes(cube, other_cube)
        if nc:
            remove_list += [other_cube]
            append_list += nc
        elif r:
            remove_list += [other_cube]
    if instructions[i]:
        append_list += [cube]
    for item in append_list:
        final_cubes.append(item)
    for item in remove_list:
        final_cubes.remove(item)

nb_on = 0
for c in final_cubes:
    nb_on += (c[0][1] - c[0][0] + 1) * (c[1][1] - c[1][0] + 1) * (c[2][1] - c[2][0] + 1)

sol2 = nb_on
part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {sol2} ({part2_time:.4f}s after part1)")
