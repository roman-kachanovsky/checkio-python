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


def ciel_solution(data):
    if len(data) == 0: return 0
    return data[0] + ciel_solution(data[1:])


def erik_white_2014_solution(data):
    d = map(str, data)
    return eval('+'.join(d))
