""" --- The Angles of a Triangle --- Simple

You are given the lengths for each side on a triangle.
You need to find all three angles for this triangle. If the given side
lengths cannot form a triangle (or form a degenerated triangle),
then you must return all angles as 0 (zero). The angles should be
represented as a list of integers in ascending order.
Each angle is measured in degrees and rounded to the nearest
integer number (Standard mathematical rounding).


Input:              The lengths of the sides of a triangle as integers.
Output:             Angles of a triangle in degrees as sorted list of integers.
How it is used:     This is a classical geometric task. The ideas can be useful
                    in topography and architecture. With this concept you can
                    measure an angle without the need for a protractor.
Precondition:       0 < a,b,c <= 1000

"""


def my_solution(a, b, c):
    import math

    cos_a = float(b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    cos_b = float(c ** 2 + a ** 2 - b ** 2) / (2 * c * a)
    cos_c = float(a ** 2 + b ** 2 - c ** 2) / (2 * a * b)

    try:
        angle_a = int(round(math.degrees(math.acos(cos_a))))
        angle_b = int(round(math.degrees(math.acos(cos_b))))
        angle_c = int(round(math.degrees(math.acos(cos_c))))
    except ValueError:
        return [0, 0, 0]

    angles = sorted([angle_a, angle_b, angle_c])

    if 0 in angles or 180 in angles:
        return [0, 0, 0]

    return angles


# TODO: Investigate most clear solution here:
# https://py.checkio.org/mission/triangle-angles/publications/review/clear/
