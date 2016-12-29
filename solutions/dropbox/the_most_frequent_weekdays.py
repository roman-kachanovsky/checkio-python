""" --- The Most Frequent Weekdays --- Simple

What is your favourite day of the week? Check if it's
the most frequent day of the week in the year.

You are given a year as integer (e. g. 2001).
You should return the most frequent day(s) of the week
in that year. The result has to be a list of days sorted
by the order of days in week (e. g. ['Monday', 'Tuesday']).
Week starts with Monday.

Input:              Year as an int.
Output:             The list of most frequent days sorted
                    by the order of days in week (from Monday
                    to Sunday).
Preconditions:      Year is between 1 and 9999. Week starts
                    with Monday.

"""


def my_solution(year):
    from datetime import date, timedelta
    from calendar import day_name

    def all_days(year):
        d = date(year, 1, 1)
        while d.year == year:
            yield d.weekday()
            d += timedelta(days=1)

    flattened_year = list(all_days(year))
    weekday_rates = map(lambda x: flattened_year.count(x), xrange(7))
    return [day_name[i] for i, d in enumerate(weekday_rates) if d == max(weekday_rates)]


def siebenschlaefer_solution(year):
    import calendar

    weekdays = [calendar.weekday(year, 1, 1)]
    if calendar.isleap(year):
        weekdays.append(calendar.weekday(year, 1, 2))
    return [calendar.day_name[i] for i in sorted(weekdays)]


def gyahun_dash_solution(year):
    from calendar import day_name, isleap, weekday

    days = (weekday(year, 1, 1 + i) for i in range(1 + isleap(year)))
    return [day_name[d] for d in sorted(days)]


def fpob_solution(year):
    import datetime, calendar

    days = [datetime.date(year, 1, 1)]
    if calendar.isleap(year):
        days.append(datetime.date(year, 1, 2))
    return [d.strftime("%A") for d in sorted(days, key=lambda d: d.weekday())]
