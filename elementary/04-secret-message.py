""" 04. --- Secret Message --- Elementary

You are given a chunk of text. Gather all capital letters in one word
in the order that they appear in the text.
For example:
    text = "How are you? Eh, ok. Low or Lower? Ohhh.",
    if we collect all of the capital letters,
    we get the message "HELLO".

Input:              A text as a string (unicode).
Output:             The secret message as a string or an empty string.
How it is used:     This is a simple exercise in working with strings:
                    iterate, recognize and concatenate.
Precondition:       0 < len(text) <= 1000
                    all(ch in string.printable for ch in text)

"""


def my_solution(text):
    return ''.join([c for c in text if c.isupper()])


veky_solution = lambda text: ''.join(filter(str.isupper, text))
