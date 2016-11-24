""" --- Saw the stick --- Elementary

The robots want to saw the stick in several pieces.
The length of the stick is N inches. We should help our
robots saw the stick. All of the parts should have integer
lengths (1, 2, 3 .. inches, but not 1.2). As we love
the numerical series and especially the Triangular numbers
(read more about Triangular numbers on Wikipedia), you
should saw the stick so that the lengths form the consecutive
fragment of the Triangular numbers series with the maximum
quantity (fragment's length). The parts should have different
lengths (no repeating). For example: 64 should divided
at 15, 21, 28, because 28, 36 is shorter and 1, 3, 15, 45
is not a consecutive fragment.

You are given a length of the stick (N). You should return
the list of lengths (integers) for the parts in ascending order.
If it's not possible and the problem does not have a solution,
then you should return an empty list.

Input:              A length of the stick as an integer.
Output:             A fragment of the Triangular numbers as a list
                    of integers (sorted in ascending order)
                    or an empty list.
How it is used:     In this task you will learn about triangular
                    numbers. A triangular number or triangle number
                    counts the objects that form an equilateral
                    triangle. This is an interesting sequence
                    which has various applications.
                    Here's a real world application: In a competitive
                    tournament format that uses a round-robin group
                    stages, the number of matches that need to be played
                    between n teams is equal to the triangular number
                    Tn-1. For example, a group stage with 4 teams
                    requires 6 matches, and a group stage with 8 teams
                    requires 28 matches.
Precondition:       0 < length < 1000

"""


def my_solution(number):
    def triangle_numbers(num):
        a, b, i = 1, 3, 3
        while a < num:
            yield a
            a, b, i = b, b + i, i + 1

    sequence = list(triangle_numbers(number))
    result = []

    for m in xrange(2, len(sequence) + 1):
        for n in xrange(len(sequence) - m + 1):
            if sum(sequence[n:n+m]) == number:
                result.append(sequence[n:n+m])

    return sorted(result, key=len)[-1] if result else []


# TODO: Investigate most clear solution here:
# https://py.checkio.org/mission/stick-sawing/publications/category/clear/
