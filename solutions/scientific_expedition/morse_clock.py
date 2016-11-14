""" --- Morse Clock --- Simple

Help Stephen to create a module for converting a normal time string
to a morse time string. As you can see in the illustration, a gray
circle means on, while a white circle means off. Every digit in
the time string contains a different number of slots. The first digit
for the hours has a length of 2 while the second digit for the hour
has a length of 4. The first digits for the minutes and seconds have
a length of 3 while the second digits for the minutes and seconds
have a length of 4. Every digit in the time is converted to binary
representation. You will convert every on (or 1) signal to dash ("-")
and every off (or 0) signal to dot (".").

An time string could be in the follow formats: "hh:mm:ss", "h:m:s"
or "hh:m:ss". The "missing" digits are zeroes. For example, "1:2:3"
is the same as "01:02:03".

The result will be a morse time string with specific format:
"h h : m m : s s"
where each digits represented as sequence of "." and "-"

Input:              A normal time string as a string (unicode).
Output:             The morse time string as a string.
How it is used:     Did you see the binary clocks task earlier?
                    This is can be a fun gift for any geek. We tried
                    to combine the old good Morse code with a binary
                    clock in this task, and now you can create
                    the new more complex binary clock, which
                    doesn't show time -- but makes morse style
                    bips and beeps. ;-)
Precondition:       time_string contains correct time.

"""


def my_solution(time_string):
    from datetime import datetime

    def _translate_to_morse(n, pos=4):
        a, b = n
        a = bin(int(a)).replace('0b', '').zfill(pos)
        b = bin(int(b)).replace('0b', '').zfill(4)
        return ''.join(['-' if int(ch) else '.' for ch in a]) \
               + ' ' + ''.join(['-' if int(ch) else '.' for ch in b])

    hours, minutes, seconds = datetime.strptime(time_string, '%H:%M:%S')\
        .strftime('%H:%M:%S').split(':')

    return ' : '.join([_translate_to_morse(hours, pos=2),
                       _translate_to_morse(minutes, pos=3),
                       _translate_to_morse(seconds, pos=3)])


# TODO: Investigate most clear solution here:
# https://py.checkio.org/mission/morse-clock/publications/review/clear/
