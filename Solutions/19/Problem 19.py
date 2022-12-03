'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

# Can solve this with "Zeller's Congruence" https://en.wikipedia.org/wiki/Zeller%27s_congruence
from math import floor

def weekday(date_of_month, month, year):
    '''Given three integers, returns an integer corresponding to the day of the week.
    Monday = 1, Sunday = 7'''
    # jan and feb are treated as 13th and 14th months of previous year for the congruence
    if month < 3:
        month += 12
        year -= 1
    
    q = date_of_month
    m = month
    K = year % 100
    J = floor(year / 100)
    
    h = (q + floor(13 * (m + 1) / 5) + K + floor(K/4) + floor(J/4) + 5*J) % 7
    
    return (h + 5) % 7 + 1 # convert so 1 is monday

Sunday = 7
tot = 0
for year in range(1901, 2000 + 1):
    for month in range(1, 12 + 1):
        if weekday(1, month, year) == Sunday:
            tot += 1
print(f"There were {tot} Sundays that fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)!")
