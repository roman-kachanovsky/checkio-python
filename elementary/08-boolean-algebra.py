''' 08. --- Boolean Algebra --- Elementary

In this mission you should implement some boolean operations.

You are given two boolean values x and y as 1 or 0 and you are given 
an operation name as described earlier. 
You should calculate the value and return it as 1 or 0.

Input:              Three arguments. X and Y as 0 or 1. 
                    An operation name as a string.
Output:             The result as 1 or 0.
How it is used:     Here you will learn how to work with boolean 
                    values and operators. 
                    You even get to think about numbers as booleans.
Precondition:       x in (0, 1)
                    y in (0, 1)
                    operation in ("conjunction", "disjunction", 
                        "implication", "exclusive", "equivalence")

'''

# My solution:
OPERATION_NAMES = ("conjunction", 
    "disjunction", 
    "implication", 
    "exclusive", 
    "equivalence")

def boolean(x, y, operation):
    if (x in (0, 1)) and (y in (0, 1)):
        if operation in OPERATION_NAMES:
            if operation == 'conjunction':
                return x and y
            elif operation == 'disjunction':
                return x or y
            elif operation == 'implication':
                if x:
                    return y
                else:
                    return 1
            elif operation == 'exclusive':
                if x == y:
                    return 0
                else:
                    return 1
            elif operation == 'equivalence':
                if x != y:
                    return 0
                else:
                    return 1

# Sim0000's solution:
def boolean(x, y, operation):
    if operation == "conjunction": return x & y
    if operation == "disjunction": return x | y
    if operation == "implication": return (1 ^ x) | y
    if operation == "exclusive":   return x ^ y
    if operation == "equivalence": return x ^ y ^ 1
    return 0

# penguinand's solution:
def boolean(x, y, operation):
    results = {"conjunction" : x and y,
               "disjunction" : x or y,
               "implication" : y or not x,
               "exclusive"   : x ^ y,
               "equivalence" : x == y
    }
    return results[operation]

# Cjkjvfnby's solution:
from operator import and_, or_, xor, eq

def implication(x, y):
    return not x or y

OPERATIONS = {"conjunction": and_,
              "disjunction": or_,
              "implication": implication,
              "exclusive": xor,
              "equivalence": eq}

def boolean(x, y, operation):
    return OPERATIONS[operation](x, y)

''' To remember:

x & y           --> x and y
x | y           --> x or y
(1 ^ x) | y     --> y or not x
x ^ y           --> x ^ y
x ^ y ^ 1       --> x == y

Dictionary can contains operations and even functions as values.
f.e.:
def arithmetic(x, y, func):
    def foo(x, y):
        return x * y
    d = {'foo': foo(x, y), 'bar': x + y}
    return d[func]

Module 'operator' contains some interesting operators.

'''