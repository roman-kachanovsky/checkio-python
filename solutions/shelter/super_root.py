""" --- Super Root --- Simple

Square roots, cube roots, 4th roots... each are too boring
for Nicola. He needs to find the super root! With your help
he will almost certainly find it.

The super root of a number N is the number x, such that xx = N.

The result should be accurate so that x ** x ~ N +-0.001.
Or N - 0.001 < x ** x < N + 0.001.

Input:              A number (N) as an integer.
Output:             The super root (x) as a float or an integer.
How it is used:     This concept can be useful for the cryptography.
                    And you will look how work your calculator then
                    calculate roots.
Precondition:       1 <= number <= 10 ** 10

"""


def my_solution(number):
    def check_precision(n):
        return number - 0.001 < n ** n < number + 0.001

    a, b = 1.0, 10.0

    if check_precision(a):
        return a

    if check_precision(b):
        return b

    x = (a + b) / 2

    while not check_precision(x):
        if x ** x > number:  # Get left part of range
            a, b = a, x
            x = (a + b) / 2
        elif x ** x < number:  # Get right part of range
            a, b = x, b
            x = (a + b) / 2
        else:
            return x
    return x


def gyahun_dash_solution(number):
    from math import log, log10

    x = log10(number) + 1

    while True:
        y = x ** x
        diff = y - number
        if abs(diff) < 0.001:
            return x
        x -= diff / (y * (1 + log(x)))


def gyahun_dash_solution_v2(number, lower=1, upper=10):
    while True:
        x = (lower + upper) / 2
        diff = x ** x - number
        if abs(diff) < 0.001:
            return x
        lower, upper = (lower, x) if diff > 0 else (x, upper)
