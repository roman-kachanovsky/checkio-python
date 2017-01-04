""" --- Ore in the desert --- Challenging

During their adventure, the Robo-trio came across a desert,
and the ships sensors have registered ore in the region.
The desert has a size of 10x10 cells and can be represented
as a 2D array. The ship has four probes which can be used
to help us find the ore. At each step you will need to return
the coordinates of a cell (as [row, column]) for the probe
to travel to. If the cell contains ore, then you can finish;
else the probe will give a distance to the location of
the ore cell (it will be the Euclidean distance between cells'
centers). The perception of probe is not very good and it will
give you a result rounded to the closest integer (1.41 ~ 1;
2.83 ~ 3). At each step you receive information from the previous
probes as a list of list. Each list will be in the following
format: [row, column, distance]. At the beginning of the mission,
you will only receive an empty list.


Input:              Information of the previous probes as a list
                    of lists. Each list contains three integers.
Output:             The coordinate of the next probe as a list
                    of two integers.
How it is used:     This task illustrates trilateration. Trilateration
                    is the process of determining absolute or relative
                    locations of points by measurement of distances,
                    using the geometry of circles, spheres or triangles.
                    In addition to being an interesting geometric problem,
                    trilateration does have practical applications
                    in surveying and navigation and is an important part
                    of the equations making global positioning systems
                    (GPS) possible.
Precondition:       len(desert) == 10
                    all(len(row) == 10 for row in desert)
                    There is always exist an ore cell in the desert.

"""


def my_solution(previous):
    from math import sin, cos, pi

    def available_circum_points(x, y, r):
        points = [(
                      int(round(cos(2 * pi / 100 * i) * r) + x),
                      int(round(sin(2 * pi / 100 * i) * r) + y)
                  ) for i in xrange(100)]
        return {p for p in points if 0 <= p[0] < 10 and 0 <= p[1] < 10}

    if previous:
        visited_points = [(s[0], s[1]) for s in previous]
        possible_targets = [available_circum_points(*s) for s in previous]
        filtered_targets = [t for t in set.intersection(*possible_targets) if t not in visited_points]
        return filtered_targets[0] if filtered_targets else [5, 3]
    return [5, 3]


def bryukh_solution(data):
    from math import hypot

    cells = [[i, j] for i in range(10) for j in range(10)]
    for x, y, d in data[-1:]:
        cells = [[i, j] for i, j in cells if round(hypot(x - i, y - j), 0) == d]
    return cells[0]
