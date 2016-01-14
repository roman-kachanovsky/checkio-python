''' 03. --- Even the last --- Elementary

You are given an array of integers. You should find the sum of the elements with even indexes (0th, 2nd, 4th...) 
then multiply this summed number and the final element of the array together. 
Don't forget that the first element has an index of 0.
For an empty array, the result will always be 0 (zero).

Input:              A list of integers.
Output:             The number as an integer.
How it is used:     Indexes and slices are important elements of coding in python and other languages. This will come in handy down the road!
Precondition:       0 <= len(array) <= 20
                    all(isinstance(x, int) for x in array)
                    all(-100 < x < 100 for x in array)
'''

# My solution:
def checkio(array):
    if len(array) == 0:
        return 0
    return sum(array[::2]) * array[len(array)-1]

# monkshorin's solution:
def checkio(array):
    if len(array) == 0: return 0
    return sum(array[0::2]) * array[-1]

# aggelgian's solution:
checkio=lambda x: sum(x[::2])*x[-1] if x else 0
