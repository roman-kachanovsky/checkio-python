""" 05. --- Xs and Os Referee ---  Simple

Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two
players (X and O) who take turns marking the spaces in a 3*3 grid.
The player who succeeds in placing three respective marks
in a horizontal, vertical, or diagonal rows (NW-SE and NE-SW)
wins the game.

But we will not be playing this game. You will be the referee
for this games results. You are given a result of a game and you must
determine if the game ends in a win or a draw as well as who will be
the winner. Make sure to return "X" if the X-player wins and "O" if the
O-player wins. If the game is a draw, return "D".

A game's result is presented as a list of strings,
where "X" and "O" are players' marks and "." is the empty cell.

Input:              A game result as a list of strings (unicode).
Output:             "X", "O" or "D" as a string.
How it is used:     The concepts in this task will help you when
                    iterating data types. They can also be used
                    in game algorithms, allowing you to know how
                    to check results.

"""


def my_solution(game_result):
    grid = ['', '', '', '', '']
    grid[0] = game_result[0][0] + game_result[1][1] + game_result[2][2]
    grid[1] = game_result[0][2] + game_result[1][1] + game_result[2][0]

    for line in game_result:
        grid.append(line)
        grid[2] += line[0]
        grid[3] += line[1]
        grid[4] += line[2]

    return 'X' if 'XXX' in grid else 'O' if 'OOO' in grid else 'D'


def danieldou_solution(board):
    # First we put everything together into a single string
    x = "".join(board)

    # Next we outline the 8 possible winning combinations.
    combos = ["012", "345", "678", "036", "147", "258", "048", "246"]

    # We go through all the winning combos 1 by 1 to see if there are any
    # all Xs or all Os in the combos
    for i in combos:
        if x[int(i[0])] == x[int(i[1])] == x[int(i[2])] and x[int(i[0])] in "XO":
            return x[int(i[0])]
    return "D"


def gyahun_dash_solution(result):
    rows = result
    cols = map(''.join, zip(*rows))
    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)
    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'
