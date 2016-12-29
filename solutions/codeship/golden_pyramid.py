""" --- Golden Pyramid --- Challenging

Our Robo-Trio need to train for future journeys and treasure hunts.
Stephan has built a special flat model of a pyramid. Now the robots
can train for speed gold running. They start at the top of the pyramid
and must collect gold in each room, choose to take the left or right
path and continue down to the next level. To optimise their gold runs,
Stephan need to know the maximum amount of gold that can be collected
in one run.

Consider a tuple of tuples in which the first tuple has one integer
and each consecutive tuple has one more integer then the last.
Such a tuple of tuples would look like a triangle. You should write
a program that will help Stephan find the highest possible sum
on the most profitable route down the pyramid. All routes down
the pyramid involve stepping down and to the left or down and to
the right.

Tips: Think of each step down to the left as moving to the same
index location or to the right as one index location higher.
Be very careful if you plan to use recursion here.

Input:              A pyramid as a tuple of tuples. Each tuple
                    contains integers.
Output:             The maximum possible sum as an integer.
How it is used:     This is a classical problem which shows you
                    how to use dynamic programming. This concept
                    is a core component of many optimisation tasks.
Precondition:       0 < len(pyramid) <= 20
                    all(all(0 < x < 10 for x in row) for row in pyramid)

"""


def my_solution(pyramid):
    weights = {(i, j): pyramid[i][j] for i in xrange(len(pyramid)) for j in xrange(len(pyramid[i]))}

    def get_weight_of_path(p):
        return sum(weights[l] for l in p)

    def find_path_with_biggest_weight(g, curr_node, path):
        path = path + [curr_node]

        if curr_node[0] == len(pyramid) - 1:
            return path, get_weight_of_path(path)

        best_path, best_weight = [], 0

        for node in g[curr_node]:
            if node not in path and node[0] > curr_node[0]:
                new_path, new_weight = find_path_with_biggest_weight(g, node, path)

                if new_weight > best_weight:
                    best_path, best_weight = new_path, new_weight

        return best_path, best_weight

    graph = {}

    for m in xrange(len(pyramid)):
        for n in xrange(len(pyramid[m])):
            nodes = [(m - 1, n - 1), (m - 1, n), (m + 1, n), (m + 1, n + 1)]
            filter_mask = lambda x: (-1 not in x) and (not (not x[0] and x[1])) \
                                    and (len(pyramid) not in x) and not (x[1] > x[0])
            graph[(m, n)] = [k for k in nodes if filter_mask(k)]

    return find_path_with_biggest_weight(graph, (0, 0), [])[1]


def gyahun_dash_solution(pyramid):
    def integrate(lowerline, upperline):
        def sum_triangle(top, left, right):
            return top + max(left, right)

        return list(map(sum_triangle, upperline, lowerline, lowerline[1:]))

    return reduce(integrate, reversed(pyramid)).pop()


def zero_loss_solution(pyramid):
    py = [list(i) for i in pyramid]
    for i in reversed(range(len(py) - 1)):
        for j in range(i + 1):
            py[i][j] += (max(py[i + 1][j], py[i + 1][j + 1]))
    return py[0][0]
