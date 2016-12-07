""" --- Moore Neighbourhood --- Elementary

You are given a state for a rectangular board game grid with chips
in a binary matrix, where 1 is a cell with a chip and 0 is an empty cell.
You are also given the coordinates for a cell in the form of row
and column numbers (starting from 0). You should determine how many
chips are close to this cell. Every cell interacts with its eight
neighbours; those cells that are horizontally, vertically, or
diagonally adjacent.

Input:              Three arguments. A grid as a tuple of tuples
                    with integers (1/0), a row number and column number
                    for a cell as integers.
Output:             How many neighbouring cells have chips as an integer.
How it is used:     As we mentioned in the beginning, this idea
                    can be useful for developing board game algorithms.
                    In addition, the same principles
                    it can be useful for navigational software, or
                    geographical surveying software.
Precondition:       3 <= len(grid) <= 10
                    all(len(grid[0]) == len(row) for row in grid)

"""


def my_solution(grid, row, col):
    room = []
    # top-left corner
    if not row and not col:
        room.extend(
            [0, grid[row][col+1], grid[row+1][col], grid[row+1][col+1]]
        )
    # top edge
    if not row and 0 < col < len(grid[0])-1:
        room.extend(
            [grid[row][col-1], 0, grid[row][col+1], grid[row+1][col-1], grid[row+1][col], grid[row+1][col+1]]
        )
    # top-right corner
    if not row and col == len(grid[0])-1:
        room.extend(
            [grid[row][col-1], 0, grid[row+1][col-1], grid[row+1][col]]
        )
    # left edge
    if not col and 0 < row < len(grid)-1:
        room.extend(
            [grid[row-1][col], grid[row-1][col+1], 0, grid[row][col+1], grid[row+1][col], grid[row+1][col+1]]
        )
    # non-edge area
    if 0 < row < len(grid)-1 and 0 < col < len(grid[0])-1:
        room.extend(
            [grid[row-1][col-1], grid[row-1][col], grid[row-1][col+1], grid[row][col-1], 0, grid[row][col+1],
             grid[row+1][col-1], grid[row+1][col], grid[row+1][col+1]]
        )
    # right edge
    if 0 < row < len(grid)-1 and col == len(grid[0])-1:
        room.extend(
            [grid[row-1][col-1], grid[row-1][col], grid[row][col-1], 0, grid[row+1][col-1], grid[row+1][col]]
        )
    # bottom-left corner
    if not col and row == len(grid)-1:
        room.extend(
            [grid[row-1][col], grid[row-1][col+1], 0, grid[row][col+1]]
        )
    # bottom edge
    if row == len(grid)-1 and 0 < col < len(grid[0])-1:
        room.extend(
            [grid[row-1][col-1], grid[row-1][col], grid[row-1][col+1], grid[row][col-1], 0, grid[row][col+1]]
        )
    # bottom-right corner
    if row == len(grid)-1 and col == len(grid[0])-1:
        room.extend(
            [grid[row-1][col-1], grid[row-1][col], grid[row][col-1], 0]
        )
    return room.count(1)


def nickie_solution(grid, row, col):
    N, M = len(grid), len(grid[0])
    NEIGHBOURS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return sum(0 <= row + i < N and 0 <= col + j < M and grid[row + i][col + j] for i, j in NEIGHBOURS)


def gyahun_dash_solution(grid, row, col):
    rows = range(max(0, row - 1), min(row + 2, len(grid)))
    cols = range(max(0, col - 1), min(col + 2, len(grid[0])))
    return sum(grid[r][c] for r in rows for c in cols) - grid[row][col]


def gyahun_dash_second_solution(grid, row, col):
    rs, cs = [slice(max(0, x - 1), x + 2) for x in (row, col)]
    return sum(e for r in grid[rs] for e in r[cs]) - grid[row][col]
