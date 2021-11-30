def read_file(path: str) -> list:
    """
    Reads a txt file and returns a list containing all lines of the file, stripped from newline characters
    :param path: filename & location
    :return: list of which each element contains a line of the file, stripped from newline character
    """
    with open(path, 'r') as my_file:
        lines = my_file.readlines()
        return [x.strip('\n') for x in lines]


def extend_grid(grid, char):
    rows = len(grid) + 2
    cols = len(grid[0]) + 2
    result = [[char for i in range(cols)] for j in range(rows)]
    s = 1
    for line in grid:
        newline = [char]
        newline += line
        newline += [char]
        result[s] = newline
        s += 1
    return result


def print_grid(grid):
    for l in grid:
        print(''.join(l))


def get_subgrid(grid):
    w = len(grid[0])-2
    result = [0]*(len(grid)-2)
    for i in range(1, len(grid) - 1):
        result[i-1] = grid[i][1:(w+1)]
    return result


def replace_grid(grid, char_from, char_to):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == char_from:
                grid[i][j] == char_to
    return grid


def replace_grid_cond(grid, cond_grid, cond, char_to):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if cond_grid[i][j] == cond:
                grid[i][j] == char_to
    return grid


def same_grids(grid1, grid2):
    for i in range(0, len(grid1)):
        for j in range(0, len(grid1[0])):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True


def grid_values(grid, value):
    result = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            result += (grid[i][j] == value)
    return result
