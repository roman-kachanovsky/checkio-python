""" --- The Rows of Cakes --- Challenging

Someone has decided to bake a load of cakes and place them
on the floor. Our robots can't help but try to find a pattern
behind the cakes' disposition. Some cakes form rows, we want
to count these rows. A row is a sequence of three or more cakes
if we can draw a straight line through its centers. The greater
row takes up the smaller rows. So if we have a row with 4 cakes,
then we have only one row (not 4 by 3).

The cake locations are represented as a list of coordinates.
A coordinate is a list of two integers. You should count the rows.

Input:              Coordinates as a list of lists with two integers.
Output:             The quantity of rows as an integer.
How it is used:     This is an example of the image and pattern
                    recognition. This concept can be useful for
                    the game mechanics or if you want to write a bot
                    for games, or when transposing printed text
                    to a digital format.
Precondition:       0 < |coordinates| < 20
                    coordinates: 0 <= x, y <= 10

"""


class Row(object):
    def __init__(self, row):
        self.p1 = row[0]
        self.p2 = row[1]


def my_solution(cakes):
    from itertools import combinations
    from math import sqrt

    def is_between(a, c, b):
        def distance(m, n):
            return sqrt((m[0] - n[0]) ** 2 + (m[1] - n[1]) ** 2)
        return round(distance(a, c) + distance(c, b), 2) == round(distance(a, b), 2)

    rows = {Row(r): 0 for r in combinations(cakes, 2)}

    # Find the rows which contain more than 2 points
    for k in rows.keys():
        for cake in cakes:
            if cake not in [k.p1, k.p2] and is_between(k.p1, cake, k.p2):
                rows[k] += 1

    # Drop all excess rows
    rows = [k for k in rows.keys() if rows[k]]

    # Find fully immersed rows
    immersed_rows = []
    for a in rows:
        for b in rows:
            if a != b and is_between(b.p1, a.p1, b.p2) and is_between(b.p1, a.p2, b.p2):
                if a not in immersed_rows:
                    immersed_rows.append(a)

    return len(rows) - len(immersed_rows)


# TODO: Investigate most clear solution here:
# https://py.checkio.org/mission/cakes-rows/publications/review/clear/
