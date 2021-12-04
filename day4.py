from aoc_help import *

lines = read_file('data/input-day4.txt')

B_ROWS = 5
B_COLS = 5
NB_SIZE = 2

# part 1
numbers_to_draw = [int(x) for x in lines[0].split(',')]
print(numbers_to_draw)

boards = []
i = 2
while i < (len(lines) - 1):
    new_board = [[0 for k in range(B_COLS)] for l in range(B_ROWS)]
    for r in range(B_ROWS):
        row = lines[i+r].split()
        for c in range(B_COLS):
            new_board[r][c] = int(row[c])
    boards += [new_board]
    i += B_ROWS + 1


def check_winner(board, numbers):
    for r in range(B_ROWS):
        if len([x for x in board[r] if x in numbers]) == B_COLS:
            return True
    for c in range(B_COLS):
        col = [row[c] for row in board]
        if len([x for x in col if x in numbers]) == B_ROWS:
            return True
    return False


def get_winner():
    for i in range(B_COLS, len(numbers_to_draw)):
        for b in boards:
            if check_winner(b, numbers_to_draw[0:i]):
                print(f"Winner found: board {boards.index(b)} after {i} numbers.")
                return b, i
    return [], -1


winner, nb_drawn = get_winner()

sum = 0
for i in range(B_ROWS):
    undrawn = [x for x in winner[i] if x not in numbers_to_draw[0:nb_drawn]]
    for el in undrawn:
        sum += el

print(f"Part 1: {sum} times {numbers_to_draw[nb_drawn-1]} = {sum*numbers_to_draw[nb_drawn-1]}")

# Part 2
nb_boards = len(boards)
winning_nbs = [0]*nb_boards

for b in range(nb_boards):
    for i in range(B_COLS, len(numbers_to_draw)):
        if check_winner(boards[b], numbers_to_draw[0:i]):
            # print(f"Board {b} wins after {i} numbers")
            winning_nbs[b] = i
            break
    else:
        continue

# print(winning_nbs)
print(f"Board {winning_nbs.index(max(winning_nbs))} looses.")

looser = boards[winning_nbs.index(max(winning_nbs))]
nb_drawn = max(winning_nbs)
sum = 0
for i in range(B_ROWS):
    undrawn = [x for x in looser[i] if x not in numbers_to_draw[0:nb_drawn]]
    for el in undrawn:
        sum += el

print(f"Solution part 2: {sum*numbers_to_draw[nb_drawn-1]}")
