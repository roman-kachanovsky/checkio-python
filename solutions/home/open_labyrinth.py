""" --- Open Labyrinth ---  Challenging

The labyrinth has no walls, but bushes surround the path on each side.
If a players move into a bush, they lose. The labyrinth is presented as
a matrix (a list of lists): 1 is a bush and 0 is part of the path.
The labyrinth's size is 12 x 12 and the outer cells are also bushes.
Players start at cell (1,1). The exit is at cell (10,10). You need
to find a route through the labyrinth. Players can move in only four
directions--South (down [1,0]), North (up [-1,0]), East (right [0,1]),
West (left [0, -1]). The route is described as a string consisting
of different characters: "S"=South, "N"=North, "E"=East, and "W"=West.

Input:              A labyrinth map as a list of lists with 1 and 0.
Output:             The route as a string that contains "W", "E", "N" and "S".
How it is used:     This is a classical problem for path-finding in graphs -- Yes,
                    the maze can be represented as a graph. It can be used
                    in navigation software for a to b navigation and
                    computer games for artificial intelligence.
                    You can find your way anywhere you wish. Just divide
                    a map into square cells and mark up the "bad" cells.
Precondition:       Outer cells are pits.
                    len(labyrinth) == 12
                    all(len(row) == 12 for row in labyrinth)

"""


class Node(object):

    def __init__(self, x, y, maze_map):
        self.x = x
        self.y = y
        self.neighbours = [(x + xoffset, y + yoffset) for xoffset, yoffset in
                           ((-1, 0), (1, 0), (0, -1), (0, 1)) if not maze_map[x + xoffset][y + yoffset]]
        self.distance = None
        self.path = None
        self.visited = False


def my_solution(maze_map):
    nodes = {}

    for x in xrange(len(maze_map)):
        for y in xrange(len(maze_map)):
            if maze_map[x][y]:
                continue
            nodes[x, y] = Node(x, y, maze_map)

    current_node = nodes[1, 1]
    current_node.distance = 0
    current_node.path = []

    unvisited_nodes = set(nodes.keys())

    while True:
        distance = current_node.distance + 1
        for nx, ny in current_node.neighbours:
            if (nx, ny) not in unvisited_nodes:
                continue

            neighbour = nodes[nx, ny]

            if neighbour.distance is None or neighbour.distance > distance:
                neighbour.distance = distance
                neighbour.path = current_node.path + [(current_node.x, current_node.y)]

        current_node.visited = True
        unvisited_nodes.remove((current_node.x, current_node.y))

        if not unvisited_nodes:
            break

        available_nodes = sorted(
            [n for n in nodes.values() if not n.visited and n.distance is not None],
            key=lambda n: n.distance
        )

        if available_nodes:
            current_node = available_nodes[0]
        else:
            break

    path = nodes[10, 10].path + [(10, 10)]
    str_path = ''

    for (ax, ay), (bx, by) in zip(path, path[1:]):
        if ax == bx and ay > by:
            str_path += 'W'
        if ax == bx and ay < by:
            str_path += 'E'
        if ay == by and ax > bx:
            str_path += 'N'
        if ay == by and ax < bx:
            str_path += 'S'

    return str_path


def kumagi_solution(data):
    result = []
    dirs = [[-1, 0, "W"], [+1, 0, "E"], [0, -1, "N"], [0, +1, "S"]]

    def move(path, x, y, field):
        field[y][x] = 1
        if x == 10 and y == 10:
            result.append(path)
        for d in dirs:
            if field[y + d[1]][x + d[0]] == 0:
                move(path + d[2], x + d[0], y + d[1], field)
    move("", 1, 1, data)

    return result[0]
