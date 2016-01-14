''' 10. --- Digits Multiplication --- Elementary

You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

For example: 
    The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Input:              A positive integer.
Output:             The product of the digits as an integer.
How it is used:     This task can teach you how to solve a problem with simple data type conversion.
Precondition:       0 < number < 106
'''

# My solution:
def checkio(number):
    s = str(number)
    result = 1
    for c in s:
        if c != '0':
            result = result * int(c)
    return result

# Cjkjvfnby's solution:
from functools import reduce
from operator import mul

def checkio(number):
    return reduce(mul, (int(x) for x in str(number) if x != '0'))

# bryukh's solution:
def checkio(number):
    res = 1
    for d in str(number):
        res *= int(d) if int(d) else 1
    return res
