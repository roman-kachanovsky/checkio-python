""" --- Humpty Dumpty Form --- Elementary

After reading this fragment Nicola wants to build his
own "Humpty Dumpty". As a basis he chooses the spheroid
(read more about it on Wikipedia). We know the height
and the width (in inches) for this spheroid. For the job
at hand, Nikola needs to know how much material is required.

You can help him and create a function to calculate
the volume (cubic inches) and the surface area (square inches).

Tips:               Be careful with sin-1x -- this is arcsin.
Input:              Two arguments. A height and a width as integers.
Output:             The volume and the surface area as a list
                    of floats. The results should be accurate
                    to two decimals.
How it is used:     This is a simple math task, but we want
                    to introduce you to the splendid shape --
                    spheroid (in case you hadn't heard of it yet).
                    The prolate spheroid is the shape of the ball
                    in several sports, such as in rugby and
                    Australian football. In American football,
                    a more pointed prolate spheroid is used.
                    Several moons of the Solar system approximate
                    prolate spheroids in shape, though they
                    are actually scalene. Examples are Mimas,
                    Enceladus, and Tethys which orbit Saturn
                    and Miranda which orbits Uranus.
                    The true shape of the Earth is called an
                    Oblate Spheroid, though it is only very
                    slightly oblate. The diameter from
                    the North Pole to the South Pole (the shortest
                    diameter) is approximately 12,714 km.
                    The equatorial diameter (the longest diameter)
                    is approximately 12,756 km. This is not a big
                    difference, but it does mean the Earth is
                    not quite a sphere.
Precondition:       0 < width < 100
                    0 < height < 100

"""


def my_solution(height, width):
    import math

    volume = math.pi / 6 * width ** 2 * height

    a = width / 2.0
    c = height / 2.0

    if a == c:
        area = 4 * math.pi * a ** 2
    elif c < a:
        e = math.sqrt(1 - c ** 2 / a ** 2)
        area = 2 * math.pi * a ** 2 * (1 + (1 - e ** 2) / e * math.atanh(e))
    else:
        e = math.sqrt(1 - a ** 2 / c ** 2)
        area = 2 * math.pi * (a ** 2) * (1 + c / (a * e) * math.asin(e))

    return [round(volume, 2), round(area, 2)]


# TODO: Investigate most clear solution here:
# https://py.checkio.org/mission/humpty-dumpty/publications/category/clear/
