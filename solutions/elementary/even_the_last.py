""" 03. --- Even the last --- Elementary

You are given an array of integers. You should find the sum of the 
elements with even indexes (0th, 2nd, 4th...) then multiply this summed 
number and the final element of the array together. 
Don't forget that the first element has an index of 0.
For an empty array, the result will always be 0 (zero).

Input:              A list of integers.
Output:             The number as an integer.
How it is used:     Indexes and slices are important elements of coding 
                    in python and other languages. 
                    This will come in handy down the road!
Precondition:       0 <= len(array) <= 20
                    all(isinstance(x, int) for x in array)
                    all(-100 < x < 100 for x in array)

"""


def my_solution(array):
    return sum(array[::2]) * array[-1] if array else 0


aggelgian_solution = lambda x: sum(x[::2]) * x[-1] if x else 0
