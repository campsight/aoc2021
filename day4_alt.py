from aoc_help import *
from board import Board

lines = read_file('data/input-day4.txt')

B_ROWS = 5
B_COLS = 5

# part 1
# read numbers that will be drawn
numbers_to_draw = [int(x) for x in lines[0].split(',')]

# read the boards (object class Board)
boards = []
i = 2 # boards start at line 2
while i < (len(lines) - 1):
    new_board = [[0 for k in range(B_COLS)] for l in range(B_ROWS)]
    for r in range(B_ROWS):
        row = lines[i+r].split()
        for c in range(B_COLS):
            new_board[r][c] = int(row[c])
    boards += [Board(new_board)]
    i += B_ROWS + 1

winning_after = 0
winner = boards[0]
for i in range(min(B_COLS, B_ROWS), len(numbers_to_draw)):
    results = [b.check_winning(numbers_to_draw[0:i]) for b in boards]
    if sum(results) >= 1:
        winner = boards[results.index(True)]
        winning_after = i-1
        break

win_sum = winner.get_sum_remaining(numbers_to_draw[0:(winning_after+1)])
print(f"Part 1: {win_sum} times {numbers_to_draw[winning_after]} = {win_sum*numbers_to_draw[winning_after]}")

# part 2
winning_nbs = []
for i in range(len(boards)):
    winning_nbs += [boards[i].get_winning_nb(numbers_to_draw)]

looser = boards[winning_nbs.index(max(winning_nbs))]
loose_sum = looser.get_sum_remaining(numbers_to_draw[0:(max(winning_nbs)+1)])
print(f"Part 2: {loose_sum} times {numbers_to_draw[max(winning_nbs)]} = {loose_sum*numbers_to_draw[max(winning_nbs)]}")


