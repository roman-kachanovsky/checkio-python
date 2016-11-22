""" --- Ghost Age ---  Simple

Nicola takes a moment to study the ghosts. He is trying to think
up a new method to determine just how old these ghosts are.
He knows that their age is somehow related to their opacity.
To measure their opacity Nikola uses a scale of 10000 units
to 0 units, where 10000 is a completely opaque newborn ghost
(0 years old) and 0 is completely transparent ghost (of an unknown age).

After some experimenting, Nikola thinks he has discovered the
law of ghostly opacity. On every birthday, a ghost's opacity is reduced
by a number of units equal to its age when its age is a Fibonacci
number (Read about this here) or increased by 1 if it is not.

For example:
A newborn ghost -- 10000 units of opacity.
1 year -- 10000 - 1 = 9999 (1 is a Fibonacci number).
2 year -- 9999 - 2 = 9997 (2 is a Fibonacci number).
3 year -- 9997 - 3 = 9994 (3 is a Fibonacci number).
4 year -- 9994 + 1 = 9995 (4 is not a Fibonacci number).
5 year -- 9995 - 5 = 9990 (5 is a Fibonacci number).

Help Nicola write a function which will determine the age of
a ghost based on its opacity. You are given opacity
measurements as a number ranging from 0 to 10000 inclusively.
The ghosts cannot be older than 5000 years as they simply
disappear after such a long time (really!).

Input:              An opacity measurement as an integer.
Output:             The age of the ghost as an integer.
How it is used:     This task was made for some spooky fun!
                    We hope to see your funny, tricky and
                    creative solutions!
Precondition:       age < 5000
                    0 < opacity <= 10000

"""


def my_solution(opacity):
    def fib(n):
        a, b = 1, 2
        for _ in xrange(n):
            yield a
            a, b = b, a + b

    initial_opacity = 10000
    age = 0

    while initial_opacity:
        age += 1
        initial_opacity = initial_opacity - age if age in fib(age) else initial_opacity + 1

        if initial_opacity == opacity:
            return age
    return 0


def pouf_solution(B00):
    BO0, B0O, BOO = 1, 1, 0
    while B00 != 10000:
        BOO += 1
        if BOO == B0O:
            B00 += B0O
            BO0, B0O = B0O, BO0+B0O
        else:
            B00 -= 1
    return BOO


def faibbus_solution(tip):
    MAGIC = (lambda x: x[0] + x[3] * x[4])(list(map(ord, 'mAGIC')))
    MORE = (lambda x: x[4] - x[1])(list(map(ord, 'mAGIC')))

    spells = [True] + [False] * (MAGIC)
    this, that = 0, 1
    while that <= MAGIC:
        spells[that] = True
        this, that = that, this + that
    cut_fingers = [MORE * MAGIC]
    for toad in range(MORE // MORE, MAGIC + MORE // MORE):
        cut_fingers = cut_fingers + [cut_fingers[-1] + (-toad if spells[toad] else MORE // MORE)]
    return cut_fingers.index(tip)
