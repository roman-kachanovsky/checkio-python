""" --- Monkey Typing --- Elementary

You are given some text potentially including sensible words.
You should count how many words are included in the given text.
A word should be whole and may be a part of other word.
Text letter case does not matter. Words are given in lowercase
and don't repeat. If a word appears several times in the text,
it should be counted only once.

Input:              Two arguments. A text as a string (unicode for py2)
                    and words as a set of strings (unicode for py2).
Output:             The number of words in the text as an integer.
How it is used:     Python is a useful and powerful language
                    for text processing.
                    This mission is only a simple example of the kind
                    of text searching tools you could build.
Precondition:       0 < len(text) <= 256
                    all(3 <= len(w) and w.islower() and w.isalpha
                    for w in words)

"""


def my_solution(text, words):
    return len([w for w in words if w in text.lower()])


def sim0000_solution(text, words):
    return sum(w in text.lower() for w in words)
