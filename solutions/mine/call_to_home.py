""" --- Call to Home --- Elementary

Nicola believes that Sophia calls to Home too much and
her phone bill is much too expensive. He took the bills
for Sophia's calls from the last few days and wants
to calculate how much it costs.

The bill is represented as an array with information about
the calls. Help Nicola to calculate the cost for each
of Sophia calls. Each call is represented as a string with date,
time and duration of the call in seconds in the follow format:

"YYYY-MM-DD hh:mm:ss duration"

The date and time in this information are the start of the call.
Space-Time Communications Co. has several rules on how to calculate
the cost of calls:

    - First 100 (one hundred) minutes in one day are priced
    at 1 coin per minute;
    - After 100 minutes in one day, each minute costs 2 coins per minute;
    - All calls are rounded up to the nearest minute.
    For example 59 sec ~ 1 min, 61 sec ~ 2 min;
    - Calls count on the day when they began. For example if a call
    was started 2014-01-01 23:59:59, then it counted to 2014-01-01;

Input:              Information about calls as a tuple of strings.
Output:             The total cost as an integer.
How it is used:     This mission will teach you how to parse and analyse
                    various types data. Sometimes you don't need the full
                    data and should single out only important fragments.
Precondition:       0 < len(calls) <= 30
                    0 < call_duration <= 7200
                    The bill is sorted by datetime.

"""


def my_solution(calls):
    calls = [i.split() for i in calls]
    curr_day, minutes = '', []

    for c in calls:
        if curr_day == c[0]:
            minutes[-1] += int(c[-1]) // 60 + (int(c[-1]) % 60 > 0)
        else:
            minutes.append(int(c[-1]) // 60 + (int(c[-1]) % 60 > 0))
            curr_day = c[0]

    return sum([100 + (k - 100) * 2 if k >= 100 else k for k in minutes])


def sim0000_solution(calls):
    from collections import Counter

    db = Counter()
    for call in calls:
        day, time, duration = call.split()
        db[day] += (int(duration) + 59) // 60
    return sum(min if min < 100 else 2 * min - 100 for min in db.values())


def saklar13_solution(calls):
    days = {}
    for call in calls:
        day, _, duration = call.split()
        duration = (int(duration) + 59) // 60
        days[day] = days.get(day, 0) + duration
    return sum(max(x, x * 2 - 100) for x in days.values())
