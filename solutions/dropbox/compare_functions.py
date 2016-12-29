""" --- Compare Functions --- Simple

Two functions f and g are provided as inputs to checkio.
The first function f is the primary function and the second
function g is the backup. Use your coding skills to return
a third function h which returns the same output as f unless
f raises an exception or returns None. In this case h should
return the same output as g. If both f and g raise exceptions
or return None, then h should return None.

As a second output, h should return a status string indicating
whether the function values are the same and if either function
erred. A function errs if it raises an exception or returns
a null value (None).

The status string should be set to: "same" if f and g return
the same output and neither errs, "different" if f and g return
different outputs and neither errs, "f_error" if f errs but not g,
"g_error" if g errs but not f, or "both_error" if both err.

Input:              Two functions: f (primary) and g (backup).
Output:             A function h which takes arbitrary inputs
                    and returns a two-tuple.
How it is used:     This is an exercise in working with functions
                    as first class objects.
Precondition:       hasattr(f,'__call__');
                    hasattr(g,'__call__')

"""


def my_solution(f, g):
    def h(*args, **kwargs):
        f_res, f_err, g_res, g_err = None, False, None, False

        try:
            f_res = f(*args, **kwargs)
            f_err = f_res is None
        except:
            f_err = True

        try:
            g_res = g(*args, **kwargs)
            g_err = g_res is None
        except:
            g_err = True

        if f_err and g_err:
            return None, 'both_error'
        elif g_err or f_err:
            return (f_res, 'g_error') if g_err else (g_res, 'f_error')
        else:
            return (g_res, 'same') if f_res == g_res else (f_res, 'different')
    return h


def diz_solution(*funcs):
    def helper(*args, **kwargs):
        output = None
        status = 'same'
        for i, f in enumerate(funcs, ord('f')):
            try:
                result = f(*args, **kwargs)
            except:
                result = None

            if result is None:
                status = [chr(i), 'both']['error' in status] + '_error'
            elif output is None:
                output = result
            elif result != output:
                status = 'different'
        return output, status
    return helper
