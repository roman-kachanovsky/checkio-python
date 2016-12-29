""" --- Largest Rectangle in a Histogram --- Simple

You have a histogram. Try to find size of the biggest rectangle
you can build out of the histogram bars.

Input:              List of all rectangles hights in histogram
Output:             Area of the biggest rectangle
How it is used:     There is no way the solution you come up with
                    will be any useful in a real life. Just have
                    some fun here.
Precondition:       0 < len(data) < 1000

"""


def my_solution(histogram):
    res = []
    for i in xrange(1, len(histogram) + 1):
        for j in xrange(len(histogram) + 1 / i):
            sliced_list = histogram[j:j+i]
            if len(sliced_list) == i:
                res.append(min(sliced_list) * i)
    return max(res)


def mof_solution(h):
    result = min(h) * len(h)
    for w in range(1, len(h)):
        for i in range(len(h) - w + 1):
            result = max(result, min(h[i:i + w]) * w)
    return result
