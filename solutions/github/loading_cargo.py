""" --- Loading Cargo --- Moderate

You have been given a list of integer weights. You should help
Stephen distribute these weights into two sets, such that
the difference between the total weight of each set is as low
as possible.

Input data:         A list of the weights as a list of integers.
Output data:        The number representing the lowest possible
                    weight difference as a positive integer.
How it is used:     This is a combinatorial optimization version
                    of the partition problem. The combinatorial
                    optimization has wide usage and you often see
                    it when you look at automated schedules or
                    route calculating.
Precondition:       0 < len(weights) <= 10
                    all(0 < x < 100 for x in weights)

"""


def my_solution(data):
    from itertools import permutations

    curr_min = sum(data)

    for prm in permutations(data):
        for i in xrange(1, len(prm)):
            delta = max(sum(prm[:i]), sum(prm[i:])) - min(sum(prm[:i]), sum(prm[i:]))
            if delta < curr_min:
                curr_min = delta
                if not curr_min:  # Optional instruction for better performance
                    return 0
    return curr_min


# TODO: Investigate most clear solution here:
# https://py.checkio.org/mission/loading-cargo/publications/category/clear/
