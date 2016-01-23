''' 11. --- Count Inversions --- Simple

You are given a sequence of unique numbers and you should count 
the number of inversions in this sequence.

Input:              A sequence as a tuple of integers.
Output:             The inversion number as an integer.
How it is used:     In this mission you will get to experience 
                    the wonder of nested loops, that is of course, 
                    if you don't use advanced algorithms.
Precondition:       2 < len(sequence) < 200
                    len(sequence) == len(set(sequence))
                    all(-100 < x < 100 for x in sequence)
'''

# My solution:
def count_inversion(sequence):
    count = 0
    for x in sequence:
        for y in sequence[sequence.index(x):]:
            if x > y:
                count += 1
    return count

# gyahun_dash's solution:
import itertools as it

def count_inversion(sequence):
    return sum(x > y for x, y in it.combinations(sequence, 2))

# bukebuer's solution:
def count_inversion(sequence):
    return sum(sum(m<n for m in sequence[i+1:]) for i,n in enumerate(sequence))

''' To remember:

itertools.combinations(iterable, r) - Return r length subsequences of 
elements from the input iterable.

>> combinations('ABCD', 2)
AB AC AD BC BD CD
>> combinations(range(4), 3)
012 013 023 123

'''
    