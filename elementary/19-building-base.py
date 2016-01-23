''' 19. --- Building Base --- Moderate

Because all the buildings in the city are rectangular and their walls 
are parallel to the streets, we can define any building using only 
the coordinates of South-Western corner as two arguments (the length of 
the west to east walls, and the length of the north to south wall) 
along with the height of the building. These values are described 
as positive numbers using conventional units. The origin point of our 
coordinate system lies in the South-West, as a result the northern 
corner ends up having the greater coordinate value than the southern 
corner. To complete this mission we need to use a couple operations. 
See the class description below.

class Building(south, west, width_WE, width_NS, height=10)
Returns a new Building instance with the South-West corner 
at [south, west] coordinates, the size is width_WE by width_NS and 
the height of the building is height. "height" is a positive number 
with a default value of 10.

    >>> Building(10, 10, 1, 2, 2)
    Building(10, 10, 1, 2, 2)
    >>> Building(0, 0, 10.5, 2.546)
    Building(0, 0, 10.5, 2.546, 10)

corners()
Returns a dictionary with the coordinates of the building corners. 
The dictionary has following keys: "north-west", "north-east", 
"south-west", "south-east". The values are lists or tuples 
with two numbers.

    >>> Building(1, 2, 2, 2).corners()
    {"north-west": [3, 2], 
    "north-east": [3, 4], 
    "south-west": [1, 2], 
    "south-east": [1, 4]}

area()
Returns the area of the building.

    >>> Building(1, 2.5, 4.2, 1.25).area()
    5.25

volume()
Returns the volume of the building.

    >>> Building(1, 2.5, 4.2, 1.25, 101).volume()
    530.25

__repr__()
This is a string representation of the Building. This method is used 
for "print" or "str" conversion. 
Returns the string in the following view: "Building({south}, {west}, 
{width_we}, {width_ns}, {height})"

    >>> str(Building(0, 0, 10.5, 2.546))
    "Building(0, 0, 10.5, 2.546, 10)"

In this mission all data will be correct and you don't need 
to implement value checking.

Input:              Statements and expression with the Building class.
Output:             The behaviour as described.
How it is used:     Here you will learn how to write a simple class 
                    with minimal functionality 
                    to achieve greater glory for Robonia.
Precondition:       All data are correct.
'''

# My solution:
class Building:
    south = 0
    west = 0
    width_WE = 0
    width_NS = 0
    height = 0
    
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):
        return {
            'north-west': [self.south + self.width_NS, self.west],   
            'north-east': [self.south + self.width_NS, self.west + self.width_WE],
            'south-west': [self.south, self.west],
            'south-east': [self.south, self.west + self.width_WE],
        }

    def area(self):
        return self.width_WE * self.width_NS

    def volume(self):
        return self.area() * self.height

    def __repr__(self):
        return 'Building({self.south}, {self.west}, {self.width_WE}, {self.width_NS}, {self.height})'.format(self=self)

# gyahun_dash's soultion:
from itertools import product

class Building(object): # W to E: width, N to S: depth
    def __init__(self, south, west, width, depth, height=10):
        self.south, self.west = south, west
        self.width, self.depth, self.height = width, depth, height
        self.north, self.east = south + depth, west + width

    def corners(self):
        pairs = product(('south', 'north'), ('west', 'east'))
        return {'-'.join(p): [getattr(self, d) for d in p] for p in pairs}

    def area(self):
        return self.width * self.depth

    def volume(self):
        return self.width * self.depth * self.height

    def __repr__(self):
        txt = 'Building({0.south}, {0.west}, {0.width}, {0.depth}, {0.height})'
        return txt.format(self)
        
''' To remember:

I can declare class properties in the __init__ "magic" method.

Other methods:
__new__(cls, [..)       - First called method, when I create a new 
                        instance. It's used fairly rarely. Usually in 
                        an immutable classes.
__init__(self, [..)     - Itinitializer.
__del__(self)           - Destructor. It doesn’t implement behavior 
                        for the statement del x. It calls when
                        GC destroys this object.

__eq__(self, other)     - Defines behavior for the equality operator ==
__ne__(self, other)     - Defines behavior for the inequality operator !=
__lt__(self, other)     - ... less-than operator <
__gt__(self, other)     - ... greater-than operator >
__le__(self, other)     - ... less-than-or-equal-to operator <=
__ge__(self, other)     - ... greater-than-or-equal-to operator >=

__pos__(self), 
__neg__(self)           - Behavior for unary +/-
__abs__(self)           - Behavior for built in abs()
__invert__(self)        - Behavior for ~
__round__(self, n)      - Behavior for round(), n is the number of
                        decimal places to round to.
__floor__(self)         - Behavior for math.floor(), rounding down to
                        the nearest integer.
__ceil__(self)          - Behavior for math.ceil(), rounding up to
                        nearest integer.
__trunc__(self)         - Behavior for math.trunc(), truncating to
                        an integer

__add__(self, other),
__sub__(self, other),
__mul__(self, other)        - Binary operators +/-/*
__floordiv__(self, other)   - Integer division using //
__div__(self, other)        - Division using /
... __mod__, __divmod__, __pow__, __lshift__, __rshift__,
__and__, __or__, __xor__

__iadd__,
__isub__,
__imul__,
...         - +=/-=/*=/... operators

__int__,
__long__,
__float__,
...         - Type conversion magic methods

__str__(self)   - str() or print()
__repr__(self)  - repr()
__hash__(self)  - hash(), has to return an integer and its result is used
                for quick key comparison in dictionaries. Live by the
                following rule: a ==b implies hash(a) == hash(b)
__bool__(self)   - bool()
__dir__(self)   - dir(), should return a list of attributes for the user
__getattr__,
__setattr__,
__delattr__     - f.e. I may check values before changing of attributes

__len__(self)   - len()
__getitem__(self, key),
__setitem__(self, key),
__delitem__(self, key)  - Behavior like d['key'] in dictionaries
__iter__(self)  - Shoul return an iterator for the container.


'''
