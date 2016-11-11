""" --- Restricted Sum --- Simple

Our new calculator is censored and as such it does not accept certain words.
You should try to trick by writing a program to calculate the sum of numbers.

Given a list of numbers, you should find the sum of these numbers.
Your solution should not contain any of the banned words, even as a part
of another word.

The list of banned words are as follows:
    sum
    import
    for
    while
    reduce

Input:              A list of numbers.
Output:             The sum of numbers.
How it is used:     This task challenges your creativity to come up
                    with a solution to fit this mission's specs!
Precondition:       The small amount of data. Let's creativity win!

"""


def my_solution(data):
    s = '%s ' * len(data)
    return eval('+'.join((s % tuple(data)).split()))


# TODO: Investigate most clear solution here:
# https://py.checkio.org/mission/restricted-sum/publications/review/clear/
