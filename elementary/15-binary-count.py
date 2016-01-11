''' 15. --- Number Base --- Simple

You are given a positive number as a string along with the radix for it. 
Your function should convert it into decimal form. The radix is less than 37 and greater than 1. 
The task uses digits and the letters A-Z for the strings.
Watch out for cases when the number cannot be converted. 
For example: "1A" cannot be converted with radix 9. For these cases your function should return -1.

Input:              Two arguments. A number as string and a radix as an integer.
Output:             The converted number as an integer.
How it is used:     Here you will learn how to work with the various numeral systems and handle exceptions.
Precondition:       re.match("\A[A-Z0-9]\Z", str_number)
                    0 < len(str_number) ≤ 10
                    2 ≤ radix ≤ 36
'''

# My solution:
def checkio(number):
    return len(str(bin(number)).replace('0', '').replace('b', ''))

# Gennady's solution:
def checkio(number):
    return bin(number).count('1')

# veky's solution:
checkio=lambda n:bin(n).count('1')
