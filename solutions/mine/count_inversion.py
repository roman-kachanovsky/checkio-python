""" --- Count Inversion --- Simple

You are given a sequence of unique numbers and you should count
the number of inversions in this sequence.

Input:              A sequence as a tuple of integers.
Output:             The inversion number as an integer.
How it is used:     In this mission you will get to experience
                    the wonder of nested loops, that is of course,
                    if you don't use advanced algorithms.
Precondition:       2 < len(sequence) < 200
                    len(sequence) == len(set(sequence))
                    all(-100 < x < 100 for x in sequence)

"""


def my_solution(s):
    return sum(x > y for x in s for y in s[s.index(x):])


def bukebuer_solutiin(sequence):
    return sum(sum(m < n for m in sequence[i + 1:]) for i, n in enumerate(sequence))


def gyahun_dash_solution(sequence):
    from itertools import combinations
    return sum(x > y for x, y in combinations(sequence, 2))
