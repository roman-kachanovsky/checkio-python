""" --- Inside Block --- Challenging

When it comes to city planning it's import to understand
the borders of various city structures. Parks, lakes or
living blocks can be represented as closed polygon and
can be described using cartesian coordinates on a map.
We need functionality to determine is a point (a building
or a tree) lies inside the structure.

For the purpose of this mission, a city structure may
be considered a polygon represented as a sequence of vertex
coordinates on a plane or map. The vertices are connected
sequentially with the last vertex in the list connecting
to the first. We are given the coordinates of the point which
we need to check. If the point of impact lies on the edge
of the polygon then it may be considered inside it.
For this mission, you need to determine whether the given
point lies inside the polygon.

Input:              Two arguments. Polygon coordinates as a tuple
                    of tuples with two integers each. A checking
                    point coordinates as a tuple of two integers.
Output:             Whatever the point inside the polygon or not
                    as a boolean.
How it is used:     This concept is using for image recognizing.
                    But as we said early it can be useful for
                    topographical software and city planning.
Precondition:       all(x >= 0 and y >= 0 for x, y in polygon)
                    point[0] >= 0 and point[1] >= 0

"""


def my_solution(polygon, point):
    from math import sqrt

    def distance(a, b):
        return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    # Check corners
    if point in polygon:
        return True

    p1_x, p1_y = polygon[0]
    inside = False

    for i in xrange(len(polygon) + 1):
        p2_x, p2_y = polygon[i % len(polygon)]

        # Check border
        if distance((p1_x, p1_y), point) + distance(point, (p2_x, p2_y)) == distance((p1_x, p1_y), (p2_x, p2_y)):
            return True

        if point[0] <= max(p1_x, p2_x) and min(p1_y, p2_y) < point[1] <= max(p1_y, p2_y):
            if p1_x == p2_x or (p1_y != p2_y and point[0] <= (point[1] - p1_y) * (p2_x - p1_x) / (p2_y - p1_y) + p1_x):
                inside = not inside
        p1_x, p1_y = p2_x, p2_y

    return inside


# TODO: Investigate most clear solution here:
# https://py.checkio.org/mission/inside-block/publications/category/clear/
