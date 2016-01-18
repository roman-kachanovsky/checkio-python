''' 09. --- Pawn Brotherhood --- Simple

Chess is a two-player strategy game played on a checkered game board 
laid out in eight rows (called ranks and denoted with numbers 1 to 8) 
and eight columns (called files and denoted with letters a to h) 
of squares. Each square of the chessboard is identified by a unique 
coordinate pair - a letter and a number (ex, "a1", "h8", "d6"). 
For this mission we only need to concern ourselves with pawns. 
A pawn may capture an opponent's piece on a square diagonally in front 
of it on an adjacent file, by moving to that square. For white pawns 
the front squares are squares with greater row than their.

A pawn is generally a weak unit, but we have 8 of them which we can use 
to build a pawn defense wall. With this strategy, one pawn defends 
the others. A pawn is safe if another pawn can capture a unit on that 
square. We have several white pawns on the chess board and only white 
pawns. You should design your code to find how many pawns are safe.

You are given a set of square coordinates where we have placed white 
pawns. You should count how many pawns are safe.

Input:              Placed pawns coordinates as a set of strings.
Output:             The number of safe pawns as a integer.
How it is used:     For a game AI one of the important tasks is the 
                    ability to estimate game state. This concept will 
                    show how you can do this on the simple chess 
                    figures positions.
Precondition:       0 < pawns <= 8

'''

# My solution:
def safe_places():
    ''' I know it's awful... '''
    tmp_dict = {(k, i): [] for k in range(1, 9) for i in range(1, 9)}
    rpl_dict = dict(zip([n for n in range(1, 9)], [m for m in 'abcdefgh']))
    sp = {}
    for k, v in tmp_dict.items():
        tmp = ''.join([str(k[0] - 1), str(k[1] - 1)])
        if not ('0' in tmp or '9' in tmp):
            v.append(''.join([rpl_dict[int(tmp[0])], tmp[1]]))
        tmp = ''.join([str(k[0] + 1), str(k[1] - 1)])
        if not ('0' in tmp or '9' in tmp):
            v.append(''.join([rpl_dict[int(tmp[0])], tmp[1]]))

        sp[''.join([rpl_dict[k[0]], str(k[1])])] = set(v)
    return sp

def safe_pawns(pawns):
    sp = safe_places()
    return sum(1 for p in pawns if sp[p].intersection(pawns))

# Pouf's solution:
def safe_pawns(pawns):
    safePawns = 0
    for pawn in pawns: # here may use 'for col, row in pawns:'
        col = pawn[0]
        row = pawn[1]

        defenseRow = str(int(row)-1)
        defenseLeft = chr(ord(col)-1) + defenseRow
        defenseRight = chr(ord(col)+1) + defenseRow

        if defenseLeft in pawns or defenseRight in pawns:
            safePawns += 1  
    return safePawns

# gyahun_dash's solution:
def getdiags(pawn):
    c, r = map(ord, pawn)
    return chr(c - 1) + chr(r - 1), chr(c + 1) + chr(r - 1)

def safe_pawns(pawns):
    return len([p for p in pawns if any(d in pawns for d in getdiags(p))])

# Kerulen's solution:
def safe_pawns(pawns):
    answer = 0
    for pawn in pawns:
        if (chr(ord(pawn[0])-1)+str(int(pawn[1])-1) in pawns 
            or chr(ord(pawn[0])+1)+str(int(pawn[1])-1) in pawns): answer +=1
    return answer

''' To remember:

ord(chr) - position of symbol in unicode table
chr(ord('a') + 1) = 'b'

I can make dictionary from two lists by
dict(zip(['a', 'b', 'c'], [1, 2, 3])) if they are same length.

I can use notation:
for n, m in [[1, 2], [3, 4], [5, 6]]:

map(func, [], ...)
>> map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])
[5, 7, 9]

'''
