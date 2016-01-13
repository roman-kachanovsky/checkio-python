''' 01. --- Non-unique Elements --- Elementary

You are given a non-empty list of integers (X). 
For this task, you should return a list consisting of only the non-unique elements 
in this list. To do so you will need to remove all unique elements 
(elements which are contained in a given list only once). 
When solving this task, do not change the order of the list. 
Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].

Input:              A list of integers.
Output:             The list of integers.
How it is used:     This mission will help you to understand how to manipulate arrays, 
                    something that is the basis for solving more complex tasks. 
                    The concept can be easily generalized for real world tasks. 
                    For example: if you need to clarify statistics by removing 
                    low frequency elements (noise).
Precondition:       0 < len(data) < 1000
'''

# My solution:
def checkio(data):
    return [el for el in data if data.count(el) > 1]

# veky's solution:
checkio=lambda d:[x for x in d if d.count(x)>1]
