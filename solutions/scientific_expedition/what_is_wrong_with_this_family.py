""" --- What is wrong with this family? --- Simple

You have a list of family relationships between father and son.
Every element on this list has two elements. The first is the
father's name, the second is a son's name. All names in the family
are unique. Check if the family tree is correct. There are
no strangers in the family tree. All connections in the family are natural.

Input:          list of lists. Every element has two strings. List
                has at least one element
Output:         bool. Is family tree correct.
Precondition:   1 <= len(tree) < 100

"""


def my_solution(tree):
    ancestor = tree[0][0]
    dict_tree = {}

    for father, son in tree:
        if dict_tree.get(father, None):
            dict_tree[father].append(son)
        else:
            dict_tree[father] = [son, ]

    fathers = dict_tree.keys()
    sons = [i for s in dict_tree.values() for i in s]

    if len(fathers) == 1:
        return True

    if set(fathers) - {ancestor, } - set(sons):
        return False

    if len(set(sons)) < len(sons):
        return False

    for k, v in dict_tree.items():
        for f in v:
            if k in dict_tree.get(f, []):
                return False

    return True


def tom_tom_solution(tree):
    fathers, sons = zip(*tree)
    fathers_set, sons_set = set(fathers), set(sons)
    return (all(father != son for father, son in tree) and
            len(fathers_set - sons_set) == 1 and
            len(sons) == len(sons_set))
