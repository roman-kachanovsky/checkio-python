""" --- Right to Left --- Elementary

You are given a sequence of strings. You should join these strings 
into chunk of text where the initial 
strings are separated by commas. As a joke on the right handed robots, 
you should replace all cases of the words "right" with the word "left", 
even if it's a part of another word. All strings are given in lowercase.

Input:              A sequence of strings as a tuple 
                    of strings (unicode).
Output:             The text as a string.
How it is used:     This is a simple example of operations 
                    using strings and sequences.
Precondition:       0 < len(phrases) < 42

"""


def my_solution(phrases):
    return ",".join(phrases).replace("right", "left")
