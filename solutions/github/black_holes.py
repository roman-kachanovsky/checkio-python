""" --- Black Holes --- Simple

You need to help Stephen implement a software model (function)
that predicts the state of black holes under a controlled environment.
The A&A research team has identified some peculiarities in the behavior
of black holes.

To create the software model one should take into account:

1.  The cartesian coordinate system is used to map out the black holes.
2.  Each black hole is represented as a circle with x, y (center
    coordinates) and r (radius).
3.  In contrast to the area, which may change during the absorption
    process, the coordinates remain constant.
4.  The area of a black hole greatly influences its mass, and
    consequently, the gravitational field.
5.  The absorption order of black holes depends on the distance between
    their centers, starting with the black holes that are closest
    to each other. If the distance between different black holes
    is equal, then the leftmost black hole in the list should merge first.
6.  The absorption process (merging) of black holes is possible if and
    only if the following conditions are met:
    - The intersection area of the two black holes is greater than
    or equal to 55% (>= 55%) of one of the two black holes area.
    - The area of one of the two black holes is over 20% (>= 20%) more
    than the area of the other.
7.  If one black hole absorbs another, their areas are summarized as
    (Stotal = S1 + S2).
8.  The absorption process continues as long as all conditions are
    met (see p. 6).

Input:              A list of tuples [(x, y, r), ..., ...],
                    where x, y - coordinates, r - radius of a black hole
Output:             Predictable (final) state of black holes as a list/tuple
                    of lists/tuples, radius should be given with two digits
                    precision as +-0.01.
How it is used:     You can use this in game development (see Agar.io example),
                    studying geometry or developing software models of real
                    physical processes.
Precondition:       1 <= len(data) <= 20
                    0.5 <= radius <= 10
                    x in [-100; 100], y in [-100; 100]

"""


def my_solution(data):
    import math
    from itertools import combinations

    def distance(x1, y1, x2, y2):
        return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

    def area(r):
        return math.pi * r ** 2

    def get_domination(c1, c2):  # Calculate domination and return it with the sorted pair of holes (big > small)
        c1_area = area(c1[2])
        c2_area = area(c2[2])
        if c1_area > c2_area:
            return round((c1_area - c2_area) / c2_area * 100, 2), c1, c2
        elif c1_area < c2_area:
            return round((c2_area - c1_area) / c1_area * 100, 2), c2, c1
        else:
            return 0.0, c1, c2

    def get_intersection(c1, c2):
        def intersection_area(x1, y1, r1, x2, y2, r2):
            d = distance(x1, y1, x2, y2)

            if d > r1 + r2:
                return 0.0  # Holes don't overlapped

            if d <= abs(r1 - r2) and r1 < r2:
                return math.pi * r1 ** 2  # First hole is completely inside second

            if d <= abs(r1 - r2) and r1 >= r2:
                return math.pi * r2 ** 2  # Second hole is completely inside first

            phi = math.acos((r1 ** 2 + d ** 2 - r2 ** 2) / (2 * r1 * d)) * 2
            theta = math.acos((r2 ** 2 + d ** 2 - r1 ** 2) / (2 * r2 * d)) * 2
            return 0.5 * theta * r2 ** 2 - 0.5 * r2 ** 2 * math.sin(theta) + \
                   0.5 * phi * r1 ** 2 - 0.5 * r1 ** 2 * math.sin(phi)

        c2_area = area(c2[2])  # Smallest hole
        int_area = intersection_area(c1[0], c1[1], c1[2], c2[0], c2[1], c2[2])
        return round(int_area / c2_area * 100, 2)

    def absorb(c1, c2):
        domination, major_hole, minor_hole = get_domination(c1, c2)
        intersection = get_intersection(major_hole, minor_hole)

        if domination >= 20 and intersection >= 55:  # Return pair of a new hole and an absorbed hole
            return (major_hole[0], major_hole[1],
                    round(math.sqrt(c1[2] ** 2 + c2[2] ** 2), 2)), minor_hole
        return None, None

    def predict_state(data):
        def change_list_of_holes(data, new_hole, absorbed_hole):
            return [new_hole if i[:2] == new_hole[:2] else i for i in data if i != absorbed_hole]

        sorted_data = sorted(
            [(c, distance(c[0][0], c[0][1], c[1][0], c[1][1])) for c in combinations(data, 2)],
            key=lambda x: (x[1], data.index(x[0][0]))
        )[:len(data)]  # Sort holes by distance and by position of each hole in list

        for pair in (i[0] for i in sorted_data):
            new_hole, absorbed_hole = absorb(pair[0], pair[1])
            if new_hole:  # Find new state of holes recursively
                return predict_state(change_list_of_holes(data, new_hole, absorbed_hole))
        return data

    return predict_state(data)


def diz_solution(data):
    from itertools import combinations as c
    from cmath import pi, acos, sqrt

    space = list(map(list, data))

    def distance(u, v):
        return abs(complex(*u[:2]) - complex(*v[:2])) + 1e-9

    def intersection(d, r1, r2):
        a = r1 ** 2 * acos((d ** 2 + r1 ** 2 - r2 ** 2) / (2 * r1 * d)) + \
            r2 ** 2 * acos((d ** 2 + r2 ** 2 - r1 ** 2) / (2 * r2 * d)) - \
            sqrt((r1 + r2 - d) * (r1 + d - r2) * (r2 + d - r1) * (d + r1 + r2)) / 2
        return a.real

    while 1:
        for d, a, b in sorted((distance(u, v), u, v) for u, v in c(space, 2)):
            (rs, s), (rb, b) = sorted((n[2], n) for n in (a, b))
            if rb ** 2 / 1.2 >= rs ** 2 <= intersection(d, rs, rb) / pi / .55:
                b[2] = abs(rs + 1j * rb)
                space.remove(s)
                break
        else:
            return space
