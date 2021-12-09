from aoc_help import *
import timeit
import numpy as np

get_input(9)
lines = read_file('data/input-day09.txt')
start_time = timeit.default_timer()

data = [x for x in lines]
gc = len(data[0])
gr = len(data)

# part 1
grid = [[0 for x in range(gc)] for y in range(gr)]
for r in range(gr):
    for c in range(gc):
        grid[r][c] = int(data[r][c])

egrid = extend_grid(grid, 9)

minlist = []
for c in range(1, gc+1):
    for r in range(1, gr+1):
        adj = [egrid[r-1][c], egrid[r][c+1], egrid[r][c-1], egrid[r+1][c]]
        el = egrid[r][c]
        if el < min(adj):
            minlist += [(r,c)]
mins = sum([egrid[m[0]][m[1]] + 1 for m in minlist])
sol1 = mins
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")


# part 2
def find_basin(grid, pos, blist):
    r, c = pos[0], pos[1]
    if r==0 or c==0 or r==(len(grid)-1) or c==(len(grid[0])-1):
        return blist
    surr = [(r-1,c), (r,c-1), (r,c+1), (r+1,c)]
    new_list = []
    for p in surr:
        if p in blist:
            continue
        if grid[p[0]][p[1]] < 9:
            blist += [p]
            new_list += [p]
    for el in new_list:
        nblist = find_basin(grid, el, blist)
        blist += [el for el in nblist if el not in blist]
    return blist


basins = []
for el in minlist:
    basins += [find_basin(egrid, el, [el])]
blen = [len(b) for b in basins]

maxp = 1
for i in range(3):
    maxb = max(blen)
    maxp *= maxb
    blen.remove(maxb)

sol2 = maxp
part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {sol2} ({part2_time:.4f}s after part1)")
