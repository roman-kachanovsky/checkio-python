""" 04. --- Min and Max --- Moderate

In this mission you should write you own py3 implementation
(but you can use py2 for this) of the built-in functions min and max.
Some builtin functions are closed here: import, eval, exec, globals.
Don't forget you should implement two functions in your code.

    max(iterable, *[, key]) or min(iterable, *[, key])
    max(arg1, arg2, *args[, key]) or min(arg1, arg2, *args[, key])

Return the largest (smallest) item in an iterable or the largest(smallest)
of two or more arguments.

If one positional argument is provided, it should be an iterable.
The largest (smallest) item in the iterable is returned.
If two or more positional arguments are provided, the largest (smallest)
of the positional arguments is returned.

The optional keyword-only key argument specifies a function of one argument
that is used to extract a comparison key from each list element
(for example, key=str.lower).

If multiple items are maximal (minimal), the function returns the first
one encountered.

Input:              One positional argument as an iterable or two
                    or more positional arguments. Optional keyword
                    argument as a function.
Output:             The largest item for the "max" function and the
                    smallest for the "min" function.
How it is used:     This task will help you understand how some of the
                    built-in functions work on a more precise level.
Precondition:       All test cases are correct and functions don't have
                    to raise exceptions.

"""


def my_solution_min(*args, **kwargs):
    key = kwargs.get('key', lambda x: x)
    args = args if len(args) > 1 else args[0]
    min_value = None
    for el in args:
        if min_value is None or key(el) < key(min_value):
            min_value = el
    return min_value


def my_solution_max(*args, **kwargs):
    key = kwargs.get('key', lambda x: x)
    args = args if len(args) > 1 else args[0]
    max_value = None
    for el in args:
        if max_value is None or key(el) > key(max_value):
            max_value = el
    return max_value


# Cjkjvfnby's solution
def get_first_from_sorted(args, key, reverse):
    if len(args) == 1:
        args = iter(args[0])
    return sorted(args, key=key, reverse=reverse)[0]


def cjkjvfnby_solution_min(*args, **kwargs):
    key = kwargs.get('key', None)
    return get_first_from_sorted(args, key, False)


def cjkjvfnby_solution_max(*args, **kwargs):
    key = kwargs.get('key', None)
    return get_first_from_sorted(args, key, True)


# yukirin's solution
from functools import reduce


def abs_method(c):
    def f(*args, **kwargs):
        key = kwargs.get('key', lambda x: x)
        if len(args) == 1: args = args[0]
        return reduce(lambda a, b: b if c(a[1], b[1]) else a, map(lambda x: (x, key(x)), args))[0]
    return f

yukirin_solution_min = abs_method(lambda a, b: a > b)
yukirin_solution_max = abs_method(lambda a, b: a < b)
