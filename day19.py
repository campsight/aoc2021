import collections
from aoc_help import *
import timeit
from scanner import Scanner

day = 19
get_input(day)
lines = read_file(f'data/input-day{day:02}.txt')
start_time = timeit.default_timer()

scanners = []
scn = Scanner(0)
for line in lines:
    if not line:
        scn.generate_rotations()
        scanners += [scn]
        continue
    if line[0:3] == "---":
        scn = Scanner(int(line.strip("---").split()[-1]))
    else:
        scn.add_beacon(*[int(x) for x in line.split(",")])
scn.generate_rotations()
scanners += [scn]

ref = scanners[0]
ref.fix_rotation(ref.get_rotations()[0])
solved = collections.deque([0])
all_solutions = {0}
absolute_beacons = set(ref.get_absolute_beacons())
to_solve = set(range(1, len(scanners)))

while to_solve:
    known = solved.pop()
    to_solve = set(range(len(scanners))).difference(all_solutions)
    for s in to_solve:
        solfound, abs_beac = scanners[known].get_overlapping2(scanners[s])
        if solfound:
            solved.append(s)
            all_solutions = all_solutions.union({s})
            absolute_beacons = absolute_beacons.union(abs_beac)

sol1 = len(absolute_beacons)
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")


# part 2
def manh_dist(p1, p2):
    return sum([abs(p1[0]-p2[0]), abs(p1[1]-p2[1]), abs(p1[2]-p2[2])])


maxdist = 0
for i in range(len(scanners)):
    for j in range(i+1, len(scanners)):
        if i == j:
            continue
        dist = manh_dist(scanners[i].get_trans_to_abs(), scanners[j].get_trans_to_abs())
        if dist > maxdist:
            maxdist = dist

sol2 = maxdist
part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {sol2} ({part2_time:.4f}s after part1)")
