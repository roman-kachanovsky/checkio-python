''' 13. --- Days Between --- Simple

You are given two dates as tuples with three numbers - year, month and day. 
For example: 
    19 April 1982 will be (1982, 4, 19). 

You should find the difference in days between the given dates. 
For example between today and tomorrow = 1 day. 
The difference will always be either a positive number or zero, so don't forget about absolute value.

Input:              Two dates as tuples of integers.
Output:             The difference between the dates in days as an integer.
How it is used:     Python has batteries included, so in this mission you will need to learn 
                    how to use completed modules so that you don't have to invent the bicycle all over again.
Precondition:       Dates between 1 january 1 and 31 december 9999. Dates are correct.
'''

# My solution:
from datetime import date

def days_diff(date1, date2):
    year, month, day = date1
    d1 = date(year=year, month=month, day=day)
    year, month, day = date2
    d2 = date(year=year, month=month, day=day)
    return abs((d2 - d1).days)

# mr.floppy's solution:
def days_diff(date1, date2):
    from datetime import date
    return abs(date(*date1) - date(*date2)).days
