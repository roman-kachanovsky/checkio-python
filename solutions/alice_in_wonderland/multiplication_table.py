""" --- Multiplication Table --- Simple

After reading "Alice's Adventures in Wonderland," our robots
decided to create their own "Multiplication table." Stephan
would lead this mission (yeah, that probably was a bad idea).
He forgot how to do multiplication and tried to invent
a new method. It's a rather strange method if we may be so blunt.

In Stephan's version of multiplication, we convert numbers
to binary representation without leading zeroes. Then the first
number is written vertically (up to down) and the second
horizontally (left to right). With that, we fill a table with
various binary operations for each crossing -- AND, OR, XOR,
so we end up with three tables. In each table we convert rows
to decimal and summarize it, then summarize the results of three
tables. Let's look at several examples.

You should help Stephan write a function to calculate this
"multiplication". You are given two positive integers (n > 0),
be careful with order of arguments.

Input:              Two arguments as integers.
Output:             The result of the Stephan's "multiplication",
                    an integer.
How it is used:     In this task we play around with logical
                    binary operations, the basis for computer
                    science. Maybe you can find a use for this
                    subject in cryptography?
Precondition:       0 < x < 100
                    0 < y < 100

"""


def my_solution(first, second):
    fst = bin(first).replace('0b', '')
    snd = bin(second).replace('0b', '')

    return sum([int(''.join(map(lambda n: str(int(m) & int(n)), snd)), 2) for m in fst]) + \
        sum([int(''.join(map(lambda n: str(int(m) | int(n)), snd)), 2) for m in fst]) + \
        sum([int(''.join(map(lambda n: str(int(m) ^ int(n)), snd)), 2) for m in fst])


# TODO: Investigate most clear solution here:
# https://py.checkio.org/mission/multiplication-table/publications/category/clear/
