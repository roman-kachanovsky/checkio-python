""" --- Flatten a list --- Elementary

Nicola likes to categorize all sorts of things. He categorized
a series of numbers and as the result of his efforts, a simple
sequence of numbers became a deeply-nested list. Sophia and Stephan
don't really understand his organization and need to figure out what
it all means. They need your help to understand Nikolas crazy list.

There is a list which contains integers or other nested lists which
may contain yet more lists and integers which then... you get the idea.
You should put all of the integer values into one flat list.
The order should be as it was in the original list with string
representation from left to right.

We need to hide this program from Nikola by keeping it small and
easy to hide. Because of this, your code should be shorter than
140 characters (with whitespaces).

Input data:         A nested list with integers.
Output data:        The one-dimensional list with integers.
How it is used:     This concept is useful for parsing and analyzing
                    files with complex structures and the task challenges
                    your creativity in writing short code.
Precondition:       0 <= |array| <= 100
                    array: -232 < x < 232 or x is a list
                    depth < 10

"""


def my_solution(a):
    return eval('[' + str(a).replace('[', '').replace(']', '') + ']')


fantakeshi_solution = lambda a: eval('[' + str(a).replace('[', '').replace(']', '') + ']')

diz_solution = f = lambda d: [d] if int == type(d) else sum(map(f, d), [])
