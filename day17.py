from aoc_help import *
import timeit
import numpy as np

day = 17
get_input(day)
lines = read_file(f'data/input-day{day:02}t.txt')
start_time = timeit.default_timer()

# target area: x=137..171, y=-98..-73
# TX = (20, 30)
# TY = (-10, -5)
TX = (137, 171)
TY = (-98, -73)




# part 1
def run_step(posx, posy, x, y):
    posx += x
    posy += y
    if x > 0:
        x -= 1
    elif x < 0:
        x += 1
    y -= 1
    return posx, posy, x, y


def is_in_target(posx, posy):
    return (TX[0] <= posx <= TX[1]) and (TY[0] <= posy <= TY[1])


def test_launch(x, y):
    maxy = 0
    posx, posy = 0, 0
    while True:
        posx, posy, x, y = run_step(posx, posy, x, y)
        if posy > maxy:
            maxy = posy
        if is_in_target(posx, posy):
            return True, maxy
        elif posx > TX[1] or posy < TY[0]:  # missed
            return False, 0


maxc = 2*abs(TY[0])
ymax, count = 0, 0
for i in range(0, maxc):
    for j in range(-maxc, maxc):
        success, ym = test_launch(i, j)
        if success and ym > ymax:
            ymax = ym
        if success:
            count += 1

sol1 = ymax
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")


# part 2

sol2 = count
part2_time = timeit.default_timer() - part1_time
print(f"Solution part 2: {sol2} ({part2_time:.4f}s after part1)")
