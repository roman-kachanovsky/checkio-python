''' 15. --- Binary count --- Simple

You are given a number (a positive integer). 
You should convert it to the binary format and count how many unities 
(1) are in the number spelling. 
For example: 5 = 0b101 contains two unities, so the answer is 2.

Input:              A number as a positive integer.
Output:             The quantity of unities in the binary form 
                    as an integer.
How it is used:     How to convert a number to the binary form. 
                    It can be useful for Computer Science purposes.
Precondition:       0 < number <= 232
'''

# My solution:
def checkio(number):
    return len(str(bin(number)).replace('0', '').replace('b', ''))

# Gennady's solution:
def checkio(number):
    return bin(number).count('1')

# veky's solution:
checkio=lambda n:bin(n).count('1')

''' To remember:

>> type(bin(n))
<class 'str'>

Function str.count('abc') calculates count of included substrings.

'''