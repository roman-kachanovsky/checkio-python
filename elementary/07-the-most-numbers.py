''' 07. --- The Most Numbers --- Elementary

You are given an array of numbers (floats). You should find 
the difference between the maximum and minimum element. 
Your function should be able to handle an undefined amount of arguments. 
For an empty argument list, the function should return 0.

Floating-point numbers are represented in computer hardware as base 
2 (binary) fractions (read about this here). 
So we should check the result with +-0.001 precision.
Think about how to work with an arbitrary number of arguments.

Input:              An arbitrary number of arguments 
                    as numbers (int, float).
Output:             The difference between maximum and minimum 
                    as a number (int, float).
How it is used:     Here you will learn about passing 
                    an undefined amount of arguments to functions.
Precondition:       0 <= len(args) <= 20
                    all(-100 < x < 100 for x in args)
                    all(isinstance(x, (int, float)) for x in args)

'''

# My solution:
def checkio(*args):
    if len(args) == 0:
        return 0
    else:
        return max(args) - min(args)

# madmanbob's solution:
def checkio(*args):
    return max(args) - min(args) if args else 0

''' To remember:

I can use 'if..else' like a generator expression's filter in any sentence.
This is one-line notation for 'if..else'.

'''