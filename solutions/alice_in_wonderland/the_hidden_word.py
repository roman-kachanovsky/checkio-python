""" --- The Hidden Word --- Simple

You are given a rhyme (a multiline string), in which lines
are separated by "newline" (\n). Casing does not matter
for your search, but whitespaces should be removed before
your search. You should find the word inside the rhyme in
the horizontal (from left to right) or vertical (from up
to down) lines. For this you need envision the rhyme as
a matrix (2D array). Find the coordinates of the word
in the cut rhyme (without whitespaces).

The result must be represented as a list --

[row_start,column_start,row_end,column_end], where

row_start is the line number for the first letter of the word.
column_start is the column number for the first letter of the word.
row_end is the line number for the last letter of the word.
column_end is the column number for the last letter of the word.
Counting of the rows and columns start from 1.
rhymes

Input:              Two arguments. A rhyme as a string and
                    a word as a string (lowercase).
Output:             The coordinates of the word.
How it is used:     This task shows the variance of the positional
                    ciphers. With this cipher you can hide
                    a message within a book which allows you
                    and receiver to send these coded messages.
Precondition:       The word is given in lowercase
                    0 < |word| < 10
                    0 < |rhyme| < 300

"""


def my_solution(text, word):
    from itertools import izip_longest

    rows = text.lower().replace(' ', '').split('\n')
    columns = [''.join(r) for r in izip_longest(*rows, fillvalue=' ')]

    for i, r in enumerate(rows, 1):
        if word in r:
            return [i, r.index(word) + 1, i, r.index(word) + len(word)]

    for k, c in enumerate(columns, 1):
        if word in c:
            return [c.index(word) + 1, k, c.index(word) + len(word), k]


# TODO: Investigate most clear solution here:
# https://py.checkio.org/mission/hidden-word/publications/category/clear/
