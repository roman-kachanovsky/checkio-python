''' 14. --- Pangram --- Simple

For this mission, we will use the latin alphabet (A-Z). 
You are given a text with latin letters and punctuation symbols. 
You need to check if the sentence is a pangram or not. Case does not matter.

Input:              A text as a string.
Output:             Whether the sentence is a pangram or not as a boolean.
How it is used:     Pangrams have been used to display typefaces, test equipment, and develop skills in handwriting, 
                    calligraphy, and keyboarding for ages.
Precondition:       all(ch in (string.punctuation + string.ascii_letters + " ") for ch in text)
                    0 < len(text)
'''

# My solution:
import string

def check_pangram(text):
    return set(string.ascii_lowercase) == set(''.join(filter(str.isalpha, text.lower())))

# dagger126's solution:
from string import ascii_lowercase
​
def check_pangram(text):
    return set(ascii_lowercase).issubset(set(text.lower()))

# saklar13's solution:
check_pangram = lambda text: len({x for x in text.lower() if x.isalpha()}) == 26

# asa19's solution:
def check_pangram(text):
    return not set('abcdefghijklmnopqrstuvwxyz') - set(text.lower())




