import copy
from collections import deque
import timeit


start_time = timeit.default_timer()

# my input
START = {2: ('B', 'A'),
         4: ('D', 'C'),
         6: ('A', 'C'),
         8: ('B', 'D')}

EMPTY = '.'
SIDES = [2, 4, 6, 8]
GOALS = {'A': 2,
         'B': 4,
         'C': 6,
         'D': 8}
COST = {'A': 1,
        'B': 10,
        'C': 100,
        'D': 1000}


def flatten_state(state):
    result = []
    for k, v in state.items():
        result += [*v]
    return ''.join(result)


def state_from_flattened(flat_state, depth):
    result = {}
    i = 0
    for n in range(11):
        if n in SIDES:
            hallpos = []
            for s in range(depth):
                hallpos += flat_state[n+i+s]
            #hallpos.reverse()
            result[n] = hallpos
            i += depth - 1
        else:
            result[n] = [flat_state[n+i]]
    return result


def get_amphipod(pos, state):
    if pos not in SIDES:
        return state[pos][0]
    if state[pos][1] != EMPTY:
        return state[pos][1]
    return state[pos][0]


def is_path_clear(pos, state, target):
    clear = True
    if pos > target:
        for i in range(target + 1, pos):
            if (i not in SIDES) and state[i][0] != EMPTY:
                clear = False
    elif pos < target:
        for i in range(pos + 1, target):
            if (i not in SIDES) and state[i][0] != EMPTY:
                clear = False
    return clear


def moves(fstate):
    cstate = state_from_flattened(fstate, 2)

    # move amphipod from the top of the room to the bottom if the amphipod is in
    # its target room (and there is no other pod at the bottom)
    for p in SIDES:
        state = copy.deepcopy(cstate)
        ap = get_amphipod(p, state)
        if state[p][1] != EMPTY and state[p][0] == EMPTY and p == GOALS[ap]:
            state[p] = [ap, EMPTY]
            yield flatten_state(state), COST[ap]
            return

    # move amphipod from the bottom of the room to the top if the top position is empty
    # and the amphipod is not in its target room
    for p in SIDES:
        state = copy.deepcopy(cstate)
        ap = get_amphipod(p, state)
        if state[p][1] == EMPTY and ap != EMPTY and p != GOALS[ap]:
            state[p] = [EMPTY, ap]
            yield flatten_state(state), COST[ap]
            return

    # if an amphipod is in the hallway, check if it can go to its (target) room.
    # Always position at the top (will be lowered by previous code block in next round).
    # The target should be empty or already contain the same amphipod, the road to
    # the hallway should be clear
    for p in range(11):
        if p in SIDES:
            continue
        ap = get_amphipod(p, state)
        if ap == EMPTY:
            continue
        target = GOALS[ap]
        tap = get_amphipod(target, state)
        if tap != EMPTY and tap != ap:
            continue
        if is_path_clear(p, state, target):
            nstate = copy.deepcopy(state)
            nstate[p] = EMPTY
            nstate[target] = [nstate[target][0], ap]
            ncost = COST[ap]*(target-p+1) if target > p else COST[ap]*(p-target+1)
            yield flatten_state(nstate), ncost

    # If an amphipod is in the top of the room and it is not its target room (or there is an other
    # amphipod below it), check to which positions in the hallway it can go (all with a clear path)
    for p in SIDES:
        state = copy.deepcopy(state)
        ap = get_amphipod(p, state)
        if ap == EMPTY: continue
        if p == GOALS[ap] and state[p][0] in (EMPTY, ap):
            continue
        for x in range(p - 1, -1, -1):
            if x in SIDES:
                continue
            if get_amphipod(x, state) != EMPTY:
                break
            nstate = copy.deepcopy(state)
            nstate[p] = [nstate[p][0], EMPTY]
            nstate[x] = [ap]
            yield flatten_state(nstate), COST[ap]*(p - x + 1)
        for x in range(p + 1, 11):
            if x in SIDES:
                continue
            if get_amphipod(x, state) != EMPTY:
                break
            nstate = copy.deepcopy(state)
            nstate[p] = [nstate[p][0], EMPTY]
            nstate[x] = [ap]
            yield flatten_state(nstate), COST[ap]*(x - p + 1)


def print_state(fstate, cost, depth):
    state = state_from_flattened(fstate, depth)
    hallway = [get_amphipod(x, state) if x not in SIDES else EMPTY for x in range(11)]
    print('#'*13, f' {cost}')
    print('#', "".join(hallway), '#', sep='')
    for i in range(depth-1, -1, -1):
        room_line = "###" if i == (depth-1) else '  #'
        for s in SIDES:
            room_line += state[s][i] + '#'
        room_line += '##' if i == (depth-1) else ''
        print(room_line)
    print('  '+'#'*9)
    print()


def part1(start: str) -> int:
    all_states = {start: (0, None)}
    queue = deque([start])
    while queue:
        state = queue.popleft()
        cost, prev = all_states[state]
        #print(f"next: {cost}, {prev}, {state}")
        # print(state, cost)
        for next, next_cost in moves(state):
            if next in all_states and all_states[next][0] <= cost + next_cost:
                continue
            all_states[next] = (cost + next_cost, state)
            queue.append(next)

    st = "..AA.BB.CC.DD.."
    path = []
    while st:
        path.append((st, all_states[st][0]))
        st = all_states[st][1]
    for st, cost in path[::-1]:
        print_state(st, cost, 2)
    return all_states["..AA.BB.CC.DD.."][0]


init = {}
for i in range(11):
    init[i] = START.get(i, ['.'])

sol1 = part1(flatten_state(init))
part1_time = timeit.default_timer() - start_time
print(f"Solution part 1: {sol1} (after {part1_time:.4f}s)")
