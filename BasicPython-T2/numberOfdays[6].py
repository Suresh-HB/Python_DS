'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-11 
@Title : Python program for number of days between two dates
'''

from datetime import date

def days_between_dates(date1, date2):
    d1 = date(*date1)
    d2 = date(*date2)
    delta = abs(d2 - d1)

    return delta.days

date1 = (2024, 7, 15)
date2 = (2023, 7, 15)

print("Number of days between", date1, "and", date2, ":", days_between_dates(date1, date2), "days")
