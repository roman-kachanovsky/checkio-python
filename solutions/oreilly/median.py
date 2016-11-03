""" 02. --- Median ---  Elementary

A median is a numerical value separating the upper half
of a sorted array of numbers from the lower half. In a list
where there are an odd number of entities, the median is the number
found in the middle of the array. If the array contains an even number
of entities, then there is no single middle value, instead the median
becomes the average of the two numbers found in the middle.
For this mission, you are given a non-empty array of natural numbers (X).
With it, you must separate the upper half of the numbers
from the lower half and find the median.

Input:              An array as a list of integers.
Output:             The median as a float or an integer.
How it is used:     The median has usage for Statistics and
                    Probability theory, it has especially significant
                    value for skewed distribution. For example: we want
                    to know average wealth of people from a set of data
                    -- 100 people earn $100 in month and 10 people
                    earn $1,000,000. If we average it out, we get
                    $91,000. This is weird value and does nothing
                    to show us the real picture. In this case
                    the median would give to us more useful value
                    and a better picture.
Precondition:       1 < len(data) <= 1000
                    all(0 <= x < 10 ** 6 for x in data)

"""


def my_solution(data):
    sorted_data = sorted(data)
    return sorted_data[len(data) / 2] if len(data) % 2 != 0 else (sorted_data[len(data) / 2 - 1] +
                                                                  sorted_data[len(data) / 2]) / 2.0


def radekj_solution(data):
    data.sort()
    half_length = len(data) / 2
    if len(data) % 2:
        return data[half_length]
    return (data[half_length] + data[half_length - 1]) / 2.0


def renelvon_solution(data):
    off = len(data) / 2
    data.sort()
    med = data[off] + data[-(off + 1)]
    return med / 2.0
