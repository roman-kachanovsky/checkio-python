''' 10. --- How to find friends --- Simple

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

'''

# My solution:
def check_connection(network, first, second):
    pairs = [[x for x in y.split('-')] for y in network]
    nodes = set([x for y in pairs for x in y])
    graph = {k: [] for k in nodes}
    for k in graph.keys():
        for p in pairs:
            if k == p[0]:
                graph[k] = p

    print(graph)

    if not graph[first] and not graph[second]:
        return False

    # def find_path(g, f, s, path=[]):
    #     path = path + [f]
    #     if not (f == s):
    #         if f in g:
    #             for node in g[f]:
    #                 new_path = find_path(g, node, s, path)
    #                 if new_path:
    #                     return True
    #     return False

    # return find_path(graph, first, second)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "scout2", "scout3") == True, "Scout Brotherhood"
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "super", "scout2") == True, "Super Scout"
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "dr101", "sscout") == False, "I don't know any scouts."

    print(check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3"))

''' To remember:


'''
