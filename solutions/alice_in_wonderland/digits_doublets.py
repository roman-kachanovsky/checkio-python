""" --- Digits Doublets --- Moderated

Doublets, sometimes known as Word ladder, is a word game
invented by Charles Dodgson (aka Lewis Carroll). A doublets
puzzle begins with two words. To solve the puzzle one must
find a chain of different words to link the two together such
that the two adjacent words differ by one letter.

For Example: FLOUR > FLOOR > FLOOD > BLOOD > BROOD > BROAD > BREAD

The Robots like using digits more than letters, so we've changed
the rules a little. You are given the list of numbers with exactly
the same length and you must find the shortest chain of numbers
to link the first number to the last like you would with the words.

For Example.
There is a list [123, 991, 323, 321, 329, 121, 921, 125, 999].
The shortest way from the first to the last is:
123 > 121 > 921 > 991 > 999

You should write a function that receives a list of numbers
(positive integers) and returns the shortest route as a list
of numbers.

Input:              Numbers as a list of integers.
Output:             The shortest chain from the first to the last
                    number as a list of integers.
How it is used:     This task is like pathfinding for numbers.
                    It shows how many things in this world can be
                    represented with mathematics, even words.
Precondition:       Numbers have the same length
                    100 <= x <= 1000

"""


def my_solution(numbers):
    def _cmp(m, n):
        return map(lambda x, y: x == y, str(m), str(n)).count(False) == 1

    last_step, steps, chains = numbers[-1], numbers[1:], [[numbers[0]]]

    while True:
        for ch in chains[:]:
            for s in steps:
                if s not in ch and _cmp(ch[-1], s):
                    chains.append(ch[:] + [s])

        if any([ch[-1] == last_step for ch in chains]):
            chains = [ch for ch in chains if ch[-1] == last_step]
            break

    return sorted(chains, key=len)[0] if chains else []


# TODO: Investigate most clear solution here:
# https://py.checkio.org/mission/digits-doublets/publications/category/clear/
