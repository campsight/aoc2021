import itertools


class Board:

    def __init__(self, matrix):
        self.board = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def check_winning(self, numbers):
        for r in range(self.rows):
            if len([x for x in self.get_rows()[r] if x in numbers]) == self.cols:
                return True
        for c in range(self.cols):
            if len([x for x in self.get_cols()[c] if x in numbers]) == self.rows:
                return True
        return False

    def get_rows(self):
        return self.board

    def get_cols(self):
        cols = []
        for i in range(self.cols):
            cols.append([row[i] for row in self.board])
        return cols

    def get_winning_nb(self, numbers):
        for i in range(min(self.cols, self.rows), len(numbers)):
            if self.check_winning(numbers[0:i]):
                return i-1
        return -1

    def get_sum_remaining(self, numbers):
        rems = itertools.chain(*[[x for x in row if x not in numbers] for row in self.get_rows()])
        if not rems:
            return 0
        return sum(rems)
