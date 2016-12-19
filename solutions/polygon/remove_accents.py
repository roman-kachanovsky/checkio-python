# -*- coding: utf-8 -*-

""" --- Remove Accents --- Simple

Assuming you are developing a user based system like facebook,
you will want to provide the functionality to search for other
members regardless of the presence of accents in a username.
Without using 3rd party collation library, you will need to remove
the accents from username before comparison.

é - letter with accent; e - letter without accent;

Input:              A phrase as a string (unicode)
Output:             An accent free Unicode string.
How it is used:     It might be a part username verification process
                    or system that propose username based on first
                    and last name of user
Precondition:       0<=|input|<=40

"""


def my_solution(msg):
    from unicodedata import normalize, category
    return u''.join(c for c in normalize('NFKD', msg) if category(c)[0] in 'LZPS')


# TODO: Investigate most clear solution here:
# https://py.checkio.org/mission/remove-accents/publications/category/clear/
