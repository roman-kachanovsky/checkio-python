''' 05. --- Secret Message --- Elementary

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

'''

# My solution:
def find_message(text):
    s = ''
    for c in text:
        if (c == c.upper()) and c.isalpha():
            s += c
    return s

# veky's solution:
find_message = lambda text: ''.join(filter(str.isupper, text))

# gyahun_dash's solution:
def find_message(text):
    return ''.join(c for c in text if c.isupper())

''' To remember:

str.isupper('T') -> True
str.isupper('t') -> False
str.isupper('Text') -> False
str.isupper('TEXT') -> True

filter() can get a function as an argument and a set of values for this
function. filter() will return values for which func(value) is True.
It's iterable object.

f.e.:
>>> filter(lambda x: x < 5, [10, 4, 2, 8]) 
[4, 2] # same as [x for x in [10, 4, 2, 8] if x < 5]

'''
