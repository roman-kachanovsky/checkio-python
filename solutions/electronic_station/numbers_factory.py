""" --- Numbers Factory --- Simple

You are given a two or more digits number N. For this mission,
you should find the smallest positive number of X, such that
the product of its digits is equal to N. If X does not exist,
then return 0.

Let's examine the example. N = 20. We can factorize this number
as 2*10, but 10 is not a digit. Also we can factorize it as 4*5
or 2*2*5. The smallest number for 2*2*5 is 225, for 4*5 -- 45.
So we select 45.

Hints:              Remember prime numbers (numbers divisible
                    by only one) and be careful with endless loops.
Input:              A number N as an integer.
Output:             The number X as an integer.
How it is used:     This task will teach you how to work with numbers
                    in code. You can factorize numbers and reconstruct
                    them into new numbers. Of course you can solve
                    this problem with brute force, but is that
                    the best way? Numbers are the foundation
                    of mathematics and programming.
Precondition:       9 < N < 10**5.

"""


def my_solution(number):
    def div(n):
        for k in xrange(9, 1, -1):
            if not n % k:
                return k, n / k
        return 1, n

    if number < 10:
        return number

    res = []

    while True:
        d, number = div(number)

        if d == 1:
            return 0
        else:
            res.append(d)

        if number < 10:
            res.append(number)
            break

    return int(''.join(str(i) for i in res[::-1]))


# TODO: Investigate most clear solution here:
# https://py.checkio.org/mission/number-factory/publications/category/clear/
