""" --- The best number ever --- Elementary

It was Sheldon's version and his best number. But you have
the coding skills to prove that there is a better number,
or prove Sheldon sheldon right. You can return any number,
but use the code to prove your number is the best!

This mission is pretty simple to solve. You are given
a function called  "checkio" which will return any number
(integer or float).

Let's write an essay in python code which will explain why
is your number is the best. Publishing the default solution
will only earn you 0 points as the goal is to earn points
through votes for your code essay.

Input:              Nothing.
Output:             A number as an integer or a float or a complex.
How it is used:     This mission revolves around code and
                    math literacy.

"""


def my_solution(n):
    def pi(precision):
        """Get pi constant with the Bailey-Borwein-Plouffe formula"""
        from decimal import Decimal, getcontext

        getcontext().prec = precision

        return sum(1 / Decimal(16) ** k * (
            Decimal(4) / (8 * k + 1) -
            Decimal(2) / (8 * k + 4) -
            Decimal(1) / (8 * k + 5) -
            Decimal(1) / (8 * k + 6)) for k in xrange(precision))

    return pi(n)
