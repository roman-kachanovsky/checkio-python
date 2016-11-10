""" --- Common Words --- Simple

Your function should find all of the words that appear in both strings.
The result must be represented as a string of words separated
by commas in alphabetic order.

Input:              Two arguments as strings.
Output:             The common words as a string.
How it is used:     Here you can learn how to work with strings and sets.
                    This knowledge can be useful for linguistic analysis.
Precondition:       Each string contains no more than 10 words.
                    All words separated by commas.
                    All words consist of lowercase latin letters.

"""


def my_solution(first, second):
    return ','.join(sorted(set(first.split(',')).intersection(set(second.split(',')))))


def ryosms_solution(first, second):
    first_set = set(first.split(","))
    second_set = set(second.split(","))
    return ",".join(sorted(first_set & second_set))
