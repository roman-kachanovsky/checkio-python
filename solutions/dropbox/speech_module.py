""" --- Speech Module --- Simple

Stephen's speech module is broken. This module is responsible for
his number pronunciation. He has to click to input all of the numerical
digits in a figure, so when there are big numbers it can take him
a long time. Help the robot to speak properly and increase his number
processing speed by writing a new speech module for him. All the words
in the string must be separated by exactly one space character.
Be careful with spaces - it's hard to see if you place
two spaces instead one.

Input:              A number as an integer.
Output:             The string representation of the number as a string.
How it is used:     This concept may be useful for the speech synthesis
                    software or automatic reports systems. This system
                    can also be used when writing a chatbot by assigning
                    words or phrases numerical values and having
                    a system retrieve responses based on those values.
Precondition:       0 < number < 1000

"""


FIRST_TEN = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
             'eight', 'nine']
SECOND_TEN = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
              'sixteen', 'seventeen', 'eighteen', 'nineteen']
OTHER_TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
              'eighty', 'ninety']
HUNDRED = 'hundred'


def my_solution(number):
    if 0 < number < 10:
        return FIRST_TEN[number - 1]

    if 9 < number < 20:
        return dict(enumerate(SECOND_TEN, 10))[number]

    if 19 < number < 100:
        return ' '.join([
            dict(enumerate(OTHER_TENS, 2))[int(str(number)[0])],
            my_solution(int(str(number)[1])),
        ]).rstrip()

    if 99 < number < 1000:
        return ' '.join([
            FIRST_TEN[int(str(number)[0]) - 1],
            HUNDRED,
            my_solution(int(str(number)[1:])),
        ]).rstrip()
    return ''


def makoto_yamagata_solution(number):
    n = number / 100
    t = [FIRST_TEN[n-1], HUNDRED] if n > 0 else []

    n = (number / 10) % 10
    t += [OTHER_TENS[n-2]] if n > 1 else []

    n = number % (10 if n > 1 else 20)
    t += [(FIRST_TEN+SECOND_TEN)[n-1]] if n > 0 else []
    return ' '.join(t)


def veky_solution(number):
    l = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
         'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
         'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
    d = dict(enumerate(l))
    d.update({30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
              80: 'eighty', 90: 'ninety'})
    h = number / 100
    if h:
        return (d[h] + ' hundred ' + veky_solution(number % 100)).strip()
    if number in d:
        return d[number]
    return d[number / 10 * 10] + ' ' + d[number % 10]
