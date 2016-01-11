''' 16. --- Number Base --- Simple

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
def checkio(str_number, radix):
    try:
        return int(str_number, radix)
    except:
        return -1

# veky's solution:
def checkio(*a):
    try: return int(*a)
    except ValueError: return -1
