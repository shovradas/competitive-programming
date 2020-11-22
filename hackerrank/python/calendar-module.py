""" Problem Link: https://www.hackerrank.com/challenges/calendar-module """

import calendar

__author__ = "Shovra Das"

m, d, y = map(int, input().split())
week_days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
print(week_days[calendar.weekday(y, m, d)])