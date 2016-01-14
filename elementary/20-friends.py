''' 20. --- Friends --- Moderate

The class "Friends" should contains names and the connections 
between them. Names are represented as strings and are case sensitive. 
Connections are undirected, so if "sophia" 
is connected with "nikola", then it's also correct in reverse.

class Friends(connections)
Returns a new Friends instance. "connections" is an iterable of sets 
with two elements in each. Each connection contains two names as strings. 
Connections can be repeated in the initial data, but inside 
it's stored once. Each connection has only two states - existing or not.

    >>> Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    >>> Friends([{"1", "2"}, {"3", "1"}])

add(connection)
Add a connection in the instance. "connection" is a set of two names 
(strings). Returns True if this connection is new. Returns False 
if this connection exists already.

    >>> f = Friends([{"1", "2"}, {"3", "1"}])
    >>> f.add({"1", "3"})
    False
    >>> f.add({"4", "5"})
    True

remove(connection)
Remove a connection from the instance. "connection" is a set 
of two names (strings). Returns True if this connection exists. 
Returns False if this connection is not in the instance.

    >>> f = Friends([{"1", "2"}, {"3", "1"}])
    >>> f.remove({"1", "3"})
    True
    >>> f.remove({"4", "5"})
    False

names()
Returns a set of names. The set contains only names which 
are connected with somebody.

    >>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "d"}))
    >>> f.names()
    {"a", "b", "c", "d"}
    >>> f.remove({"d", "c"})
    True
    >>> f.names()
    {"a", "b", "c"}

connected(name)
Returns a set of names which is connected with the given "name". 
If "name" does not exist in the instance, then return an empty set.

    >>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}))
    >>> f.connected("a")
    {"b", "c"}
    >>> f.connected("d")
    set()
    >>> f.remove({"c", "a"})
    True
    >>> f.connected("c")
    {"b"}
    >>> f.remove({"c", "b"})
    True
    >>> f.connected("c")
    set()

In this mission all data will be correct and you don't need 
to implement value checking.

Input:              Statements and expression with the Friends class.
Output:             The behaviour as described.
How it is used:     Here you will implement a class with mutable states. 
                    This is not a simple structure with a couple 
                    of functions, but object representation 
                    with more complex structure.
Precondition:       All data is correct.
'''

# My solution:
from functools import reduce

class Friends(object):
    connections = list()
    
    def __init__(self, connections):
        self.connections = list(connections)

    def add(self, connection):
        if connection in self.connections:
            return False
        else:
            self.connections.append(connection)
            return True

    def remove(self, connection):
        if not self.connections:
            return False
        elif connection in self.connections:
            self.connections.remove(connection)
            return True
        else:
            return False
            
    def names(self):
        listmerge = lambda s: reduce(lambda d,el: d.extend(el) or d, s, [])
        return set(listmerge(self.connections))

    def connected(self, name):
        output = list()
        for c in self.connections:
            if name in c:
                output.extend(c)
                output.remove(name)
        return set(output)

# gyahun_dash's solution:
class Friends(set):
    def __init__(self, pairs=set()):
        super().__init__(map(frozenset, pairs))

    def add(self, pair):
        if pair in self: return False
        super().add(frozenset(pair))
        return True

    def remove(self, pair):
        if pair not in self: return False
        super().remove(pair)
        return True

    def names(self):
        return set().union(*self)

    def connected(self, name):
        return Friends(filter({name}.issubset, self)).names() - {name}
          