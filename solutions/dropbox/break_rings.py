""" --- Break Rings --- Challenging

A blacksmith gave his apprentice a task, ordering them
to make a selection of rings. The apprentice is not yet
skilled in the craft and as a result of this, some
(to be honest, most) of rings came out connected together.
Now he's asking for your help separating the rings and
deciding how to break enough rings to free so as to get
the maximum number of rings possible.

All of the rings are numbered and you are told which
of the rings are connected. This information is given
as a sequence of sets. Each set describes the connected
rings. For example: {1, 2} means that the 1st and 2nd rings
are connected. You should count how many rings we need
to break to get the maximum of separate rings.
Each of the rings are numbered in a range from 1 to N,
where N is total quantity of rings.


Input:              Information about the connected rings
                    as a tuple of sets with integers.
Output:             The number of rings to break as an integer.
How it is used:     This model specializes in optimizing something
                    with specific conditions. Using the basic
                    concepts, you could create a model for improving
                    a transportation grid.
Precondition:       all(len(s) == 2 for s in rings)
                    sorted(reduce(set.union, rings)) == \
                    list(range(1, max(reduce(set.union, rings)) + 1))

"""


def my_solution(chain):
    def get_connecting_rings(ch):
        return {j for j in (i for subch in ch for i in subch) if len(filter(lambda x: x, (j in k for k in ch))) > 1}

    def find_shortest_list_of_broken_rings(chain, ring_to_brake, broken_rings):
        broken_rings += [ring_to_brake]
        links_for_breaking = [list(l) for l in chain if ring_to_brake in l]
        new_chain = [l for l in chain if list(l) not in links_for_breaking]

        if not new_chain:
            return broken_rings

        shortest = None

        next_connected_rings = get_connecting_rings(new_chain)

        if not next_connected_rings:
            return broken_rings + list({list(l)[0] for l in new_chain})

        for r in next_connected_rings:
            if r not in broken_rings:
                new_broken_rings = find_shortest_list_of_broken_rings(new_chain, r, broken_rings[:])
                if new_broken_rings:
                    if not shortest or len(new_broken_rings) < len(shortest):
                        shortest = new_broken_rings
        return shortest

    results = []
    for i in get_connecting_rings(chain):
        results.append(find_shortest_list_of_broken_rings(chain, i, []))
    return len(sorted(results, key=len)[0])


# TODO: Investigate most clear solution here:
# https://py.checkio.org/mission/break-rings/publications/category/clear/
