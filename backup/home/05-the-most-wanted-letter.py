''' 05. --- The Most Wanted Letter --- Simple

You are given a text, which contains different english letters 
and punctuation symbols. 
You should find the most frequent letter in the text. 
The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, 
so for the purpose of your search, "A" == "a". 
Make sure you do not count punctuation symbols, digits and whitespaces, 
only letters.

If you have two or more letters with the same frequency, 
then return the letter which comes first in the latin alphabet. 
For example -- "one" contains "o", "n", "e" only once for each, 
thus we choose "e".

Input:              A text for analysis as a string (unicode for py2.7).
Output:             The most frequent letter in lower case as a string.
How it is used:     For most decryption tasks you need to know 
                    the frequency of occurrence for various letters 
                    in a section of text. 
                    For example: we can easily crack a simple addition or 
                    substitution cipher if we know the frequency 
                    in which letters appear. 
                    This is interesting stuff for language experts!
Precondition:       A text contains only ASCII symbols.
                    0 < len(text) <= 105
'''

# My solution:
import operator

def checkio(text):
    text = ''.join([c for c in text.lower() if c.isalpha()])
    text_dict = {}
    for c in text:
        text_dict[c] = text.count(c)
    return max(sorted(text_dict.items()), key=operator.itemgetter(1))[0]

# bryukh's solution:
import string

def checkio(text):
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)

# veky's solution:
from string import ascii_lowercase as letters
checkio = lambda text: max(letters, key=text.lower().count)

''' To remember:

max(string.ascii_lowercase, key=text.count) - Letter from 
string.ascii_lowercase sends to text.count() as argument and in
result I have list of counts of letters. Then I can calculate max value.

'''
