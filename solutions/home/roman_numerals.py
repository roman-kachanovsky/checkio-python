""" --- Roman Numerals --- Moderate

Roman numerals come from the ancient Roman numbering system.
They are based on specific letters of the alphabet which are combined
to signify the sum (or, in some cases, the difference) of their values.
The first ten Roman numerals are:

    I, II, III, IV, V, VI, VII, VIII, IX, and X.

The Roman numeral system is decimal based but not directly positional
and does not include a zero. Roman numerals are based on combinations
of these seven symbols:

    Symbol  Value
    I       1 (unus)
    V       5 (quinque)
    X       10 (decem)
    L       50 (quinquaginta)
    C       100 (centum)
    D       500 (quingenti)
    M       1,000 (mille)

For this task, you should return a roman numeral using the specified
integer value ranging from 1 to 3999.

Input:              A number as an integer.
Output:             The Roman numeral as a string.
How it is used:     This is an educational task that allows you to
                    explore different numbering systems. Since roman
                    numerals are often used in the typography, it can
                    alternatively be used for text generation.
                    The year of construction on building faces and
                    cornerstones is most often written by Roman numerals.
                    These numerals have many other uses in the modern world
                    and you read about it here... Or maybe you will
                    have a customer from Ancient Rome ;-)
Precondition:       0 < number < 4000

"""


def my_solution(number):
    numeral_dict = {
        1: 'I', 2: 'II', 3: 'III', 4: 'IV',
        5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
        50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
        500: 'D', 900: 'CM', 1000: 'M'
    }

    def _get_roman_numeral(n):
        if not n:
            return ''

        for k in sorted(numeral_dict.keys(), reverse=True):
            if n % k < n:
                return numeral_dict[k] * (n / k) + _get_roman_numeral(n % k)

    return _get_roman_numeral(number)


def stefanpochmann_solution(n):
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
        result += n // arabic * roman
        n %= arabic
    return result
