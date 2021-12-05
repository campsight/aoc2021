def read_file(path: str) -> list:
    """
    Reads a txt file and returns a list containing all lines of the file, stripped from newline characters
    :param path: filename & location
    :return: list of which each element contains a line of the file, stripped from newline character
    """
    with open(path, 'r') as my_file:
        lines = my_file.readlines()
        return [x.strip('\n') for x in lines]


def bin_to_int(strbinlist: str) -> int:
    """
    Transforms a string like "0110011" to an integer (never negative)
    :param strbinlist: the string to transform
    :return: the int representation
    """
    return int('0b' + ''.join(strbinlist), 2)


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


def get_direction(c1, c2):
    if c1 == c2:
        return 0
    if c1 < c2:
        return 1
    return -1


def add_line(line: tuple, grid: list) -> None:
    """
    Adds a line to a grid by increasing every coördinate of the line in the grid with +1
    :param line: ([x1][y1], [x2][y2]) coordinates of a lines
    :param grid: [rows][columns] grid to fill/increase
    :return: Nothing, operates on the grid (list) given
    """
    x1, y1 = line[0][0], line[0][1]
    x2, y2 = line[1][0], line[1][1]
    sx = get_direction(x1, x2)
    sy = get_direction(y1, y2)
    line_len = max(abs(x1-x2), abs(y1-y2))
    for i in range(line_len+1):
        grid[x1 + (i * sx)][y1 + (i * sy)] += 1
