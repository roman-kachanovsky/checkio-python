""" --- How to find friends --- Simple

We have an array of straight connections between drones.
Each connection is represented as a string with two names of friends
separated by hyphen. For example: "dr101-mr99" means what the dr101
and mr99 are friends. Your should write a function that allow determine
more complex connection between drones. You are given two names also.
Try to determine if they are related through common bonds by any depth.
For example: if two drones have a common friends or friends who have
common friends and so on.

Input:              Three arguments: Information about friends as
                    a tuple of strings; first name as a string;
                    second name as a string.
Output:             Are these drones related or not as a boolean.
How it is used:     This concept will help you find not too obvious
                    connections with the building of bond networks.
                    And how to work social networks.
Precondition:       len(network) <= 45
                    if "name1-name2" in network,
                    then "name2-name1" not in network
                    3 <= len(drone_name) <= 6
                    first_name and second_name in network.

"""


def my_solution(network, first, second):
    def find_path(g, n):
        visited_nodes[n] = True
        for k in g[n]:
            if not visited_nodes[k]:
                find_path(g, k)

    pairs = [[x for x in y.split('-')] for y in network]
    nodes = set([x for y in pairs for x in y])
    visited_nodes = {k: False for k in nodes}
    graph = {k: [] for k in nodes}

    for k in graph.keys():
        for p in pairs:
            if k in p:
                graph[k].append(p[0]) if k != p[0] else graph[k].append(p[1])

    find_path(graph, first)
    return visited_nodes[second]


def gyahun_dash_solution(shakehands, me, you):
    from itertools import chain

    hands = {tuple(pair.split('-')) for pair in shakehands}
    amigos = {me}

    while amigos != set():
        pairs = {pair for pair in hands if any(one in pair for one in amigos)}
        amigos = set(chain(*pairs)) - amigos
        if you in amigos: return True
        hands -= pairs

    return False


def sim0000_solution(network, first, second):
    setlist = []
    for connection in network:
        s = ab = set(connection.split('-'))
        # unify all set related to a, b
        for t in setlist[:]: # we need to use copy
            if t & ab:       # check t include a, b
                s |= t
                setlist.remove(t)
        setlist.append(s)    # only s include a, b
    return any({first, second} <= s for s in setlist)
