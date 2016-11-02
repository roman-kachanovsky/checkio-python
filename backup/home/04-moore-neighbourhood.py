''' 04. --- Moore Neighbourhood --- Elementary

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
'''

# My solution:
def count_neighbours(grid, row, col):
    room = []
    # top-left corner
    if row == 0 and col == 0:
        room.extend([0, grid[row][col+1],
                    grid[row+1][col], grid[row+1][col+1]])
    # top edge
    if row == 0 and col > 0 and col < len(grid[0])-1:
        room.extend([grid[row][col-1], 0, grid[row][col+1],
                    grid[row+1][col-1], grid[row+1][col], grid[row+1][col+1]])
    # top-right corner
    if row == 0 and col == len(grid[0])-1:
        room.extend([grid[row][col-1], 0,
                    grid[row+1][col-1], grid[row+1][col]])
    # left edge
    if row > 0 and col == 0 and row < len(grid)-1:
        room.extend([grid[row-1][col], grid[row-1][col+1],
                    0, grid[row][col+1],
                    grid[row+1][col], grid[row+1][col+1]])
    # non-edge area
    if row > 0 and col > 0 and row < len(grid)-1 and col < len(grid[0])-1:
        room.extend([grid[row-1][col-1], grid[row-1][col], grid[row-1][col+1],
                    grid[row][col-1], 0, grid[row][col+1],
                    grid[row+1][col-1], grid[row+1][col], grid[row+1][col+1]])
    # right edge
    if row > 0 and row < len(grid)-1 and col == len(grid[0])-1:
        room.extend([grid[row-1][col-1], grid[row-1][col],
                    grid[row][col-1], 0,
                    grid[row+1][col-1], grid[row+1][col]])
    # bottom-left corner
    if col == 0 and row == len(grid)-1:
        room.extend([grid[row-1][col], grid[row-1][col+1],
                    0, grid[row][col+1]])
    # bottom edge
    if col > 0 and row == len(grid)-1 and col < len(grid[0])-1:
        room.extend([grid[row-1][col-1], grid[row-1][col], grid[row-1][col+1],
                    grid[row][col-1], 0, grid[row][col+1]])
    # bottom-right corner
    if row == len(grid)-1 and col == len(grid[0])-1: 
        room.extend([grid[row-1][col-1], grid[row-1][col],
                    grid[row][col-1], 0])                    
    return room.count(1)

# nickie's solution:
def count_neighbours(grid, row, col):
    N, M = len(grid), len(grid[0])
    NEIGHBOURS = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    return sum(0 <= row+i < N and 0 <= col+j < M and grid[row+i][col+j]
               for i, j in NEIGHBOURS)

# gyahun_dash's solution:
def count_neighbours(grid, row, col):
    rows = range(max(0, row - 1), min(row + 2, len(grid)))
    cols = range(max(0, col - 1), min(col + 2, len(grid[0])))
    return sum(grid[r][c] for r in rows for c in cols) - grid[row][col]

# gyahun_dash's solution:
def count_neighbours(grid, row, col):
    rs, cs = [slice(max(0, x - 1), x + 2) for x in (row, col)]
    return sum(e for r in grid[rs] for e in r[cs]) - grid[row][col]

''' To remember:

slice() - representing the set of indices specified 
by range(start, stop, step)

f.e.:
>> a = [1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
>> sl = slice(2, 5)
slice(2, 5, None)
>> a[sl]
[3, 4, 5]

'''
