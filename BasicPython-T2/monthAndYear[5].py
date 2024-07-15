'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-11 
@Title : Python program for calender
'''

import calendar

def print_calendar(year, month):
    print(calendar.month(year, month))
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
print_calendar(year, month)
