class SimpleGraph(object):
    def __init__(self, list_of_adjacencies):
        self.list_of_adjacencies = list_of_adjacencies
        self.visited_nodes = [False for x in list_of_adjacencies]
        self.path_by_steps = []

    def __str__(self):
        out = '<SimpleGraph object: \n'
        count = 0
        for x in self.list_of_adjacencies:
            out += str(count) + ' -> {'
            for k, v in x.items():
                out += str(k) + ': ' + str(v) + ', '
            out = out.rstrip(', ') + '}\n'
            count += 1
        return out.rstrip() + '>'

    def reset(self):
        self.visited_nodes = [False for x in self.list_of_adjacencies]
        self.path_by_steps = []

    def add_node(self, x, w):
        if len(self.list_of_adjacencies) <= x:
            return -1
        self.list_of_adjacencies.append({x: w})
        self.list_of_adjacencies[x][len(self.list_of_adjacencies)-1] = w
        self.reset()
        return len(self.list_of_adjacencies)-1

    def set_relation(self, x, y, w):
        if (len(self.list_of_adjacencies) <= x 
                or len(self.list_of_adjacencies) <= y
                or w <= 0):
            return False
        self.list_of_adjacencies[x][y] = w
        self.list_of_adjacencies[y][x] = w
        return True

    def remove_relation(self, x, y):
        if (len(self.list_of_adjacencies) <= x 
                or len(self.list_of_adjacencies) <= y):
            return False
        del self.list_of_adjacencies[x][y]
        del self.list_of_adjacencies[y][x]     
        return True

    def validate_relations(self):
        i = 0
        for n in self.list_of_adjacencies:
            for k, v in n.items():
                if v <= 0:
                    raise Exception('Relation {0}-{1}: Weight should be positive and non-zero.'.format(i, k))
            i += 1

    def disconnect_node(self, x):
        if len(self.list_of_adjacencies) <= x:
            return False
        self.list_of_adjacencies[x] = {}
        for n in self.list_of_adjacencies:
            if x in n.keys():
                del n[x]
        return True

    def get_weight(self, x, y):
        if (len(self.list_of_adjacencies) <= x 
                or len(self.list_of_adjacencies) <= y):
            return -1
        if x in self.list_of_adjacencies[y].keys():
            return self.list_of_adjacencies[y][x]
        else:
            return -1

    def find_path(self, start_node):
        self.visited_nodes[start_node] = True
        for k, v in self.list_of_adjacencies[start_node].items():
            if not self.visited_nodes[k]:
                self.find_path(k)

    def check_if_all_nodes_visited(self):
        return not (False in self.visited_nodes)

    def step_by_min_weight(self, node):
        tmp = sorted(self.list_of_adjacencies[node], key=self.list_of_adjacencies[node].get)
        for k in tmp:
            if not self.visited_nodes[k]:
                return k
        return node

    def find_path_by_steps(self, start_node):
        self.path_by_steps.append(start_node)
        self.visited_nodes[start_node] = True
        next_node = self.step_by_min_weight(start_node)
        if not self.visited_nodes[next_node]:
            self.find_path_by_steps(next_node)

    def get_path_by_step(self):
        return 'Path: {0}, steps: {1}'.format(self.path_by_steps, len(self.path_by_steps)-1)


if __name__ == '__main__':
    sg = SimpleGraph(
        [   
            {1: 4, 3: 3, 6: 2},     # 0
            {0: 4, 2: 4},           # 1
            {1: 4},                 # 2
            {0: 3, 4: 1},           # 3
            {3: 1},                 # 4
            {6: 1},                 # 5
            {5: 1, 0: 2},           # 6
        ]
    )
    print(sg)                       ## 1st state
    sg.add_node(0, 4)               # 7
    sg.add_node(7, 3)               # 8
    print(sg)                       ## 2nd state 
    sg.validate_relations()         
    print(sg.get_weight(0, 3))      # Related nodes only
    sg.set_relation(5, 7, 2)        # Join 5 and 7 nodes
    print(sg)                       ## 3rd state
    sg.remove_relation(7, 5)        # Disconnect 5 and 7 nodes
    print(sg)                       ## 4th state
    sg.add_node(3, 2)               # Join new 9th node and 3
    sg.set_relation(9, 2, 1)        # Join 9 and 2 nodes
    print(sg)                       ## 5th state
    sg.disconnect_node(9)           # Exclude node 9
    print(sg)                       ## 6th state

    sg.find_path(0)                 # Walk on graph
    print(sg.check_if_all_nodes_visited())  # False, because 9 node is alone
    sg.reset()                      # Reset list of visited nodes

    sg.find_path_by_steps(2)        
    print(sg.get_path_by_step())    # I expect that the last node is 5
    sg.reset()
