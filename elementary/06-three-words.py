''' 06. --- Three words --- Elementary

You are given a string with words and numbers separated by whitespaces (one space). 
The words contains only letters. You should check if the string contains three words in succession. 
For example, the string "start 5 one two three 7 end" contains three words in succession.

Input:              A string with words.
Output:             The answer as a boolean.
How it is used:     This teaches you how to work with strings and introduces some useful functions.
Precondition:       The input contains words and/or numbers. There are no mixed words (letters and digits combined).
                    0 < len(words) < 100
'''

# My solution:
def checkio(words):
    lst = words.split(' ')
    counter = 0
    for l in lst:
        if l.isalpha():
            counter += 1
            if counter == 3:
                break
        else:
            counter = 0
    return (counter == 3)

# veky's solution:
def checkio(words):
    succ = 0
    for word in words.split():
        succ = (succ + 1) * word.isalpha()
        if succ == 3: return True
    else: return False
