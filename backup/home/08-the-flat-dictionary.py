''' 08. --- The Flat Dictionary --- Simple

Python dictionaries are a convenient data type to store and process 
configurations. They allow you to store data by keys to create nested 
structures. You are given a dictionary where the keys are strings and 
the values are strings or dictionaries. The goal is flatten 
the dictionary, but save the structures in the keys. The result 
should be the a dictionary without the nested dictionaries. The keys 
should contain paths that contain the parent keys from the original 
dictionary. The keys in the path are separated by a "/". 
If a value is an empty dictionary, then it should be replaced 
by an empty string ("").

Let's look at an example:

    {
        "name": {
            "first": "One",
            "last": "Drone"
        },
        "job": "scout",
        "recent": {},
        "additional": {
            "place": {
                "zone": "1",
                "cell": "2"}
        }
    }

The result will be:

    {"name/first": "One",           #one parent
     "name/last": "Drone",
     "job": "scout",                #root key
     "recent": "",                  #empty dict
     "additional/place/zone": "1",  #third level
     "additional/place/cell": "2"}

Sophia has already written the code for this task, but it has a bug. 
You need to find and fix this bug.

Input:              An original dictionary as a dict.
Output:             The flattened dictionary as a dict.
How it is used:     This concept can be useful if you need to parse 
                    config files and simplify structures for 
                    grandfathered systems and file structures. 
                    You can easily modify this idea for your own 
                    specifications. Besides that, it's a useful skill 
                    to be able to read code and search for bugs.
Precondition:       Keys in a dictionary are non-empty strings.
                    Values in a dictionary are strings or dicts.
                    root_dictionary != {}

'''

# My solution:
def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            if isinstance(v, dict):
                # Uncomment this lines to fix a bug
                # if not v:
                #     result["/".join((path + (k,)))] = ''
                # else:
                    stack.append((path + (k,), v))
            else:
                result["/".join((path + (k,)))] = v
    return result

''' To remember:

List have a .pop(i) built-in function. It removes item from end of list,
if 'i' is not specified. Respectively .append() can use instead .push()

'''
