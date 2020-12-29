#!/bin/python3

""" problem: https://www.hackerrank.com/challenges/day-of-the-programmer """

__author__ = "Shovra Das"

def is_julian_leap_year(year):
    return year%4==0
    
def is_gregorian_leap_year(year):
    return year%400==0 or (year%4==0 and year%100!=0)

def day_of_programmer(year):
    day = 13
    if year == 1918:
        day = 26  # 12+14 => 12: 1918 is not a leap year, 14: February looses 14 days in 1918
    elif (year<1918 and is_julian_leap_year(year)) or (year>1918 and is_gregorian_leap_year(year)):
        day = 12
        
    return f"{day}.09.{year}"
    

if __name__ == '__main__':
    year = int(input())

    result = day_of_programmer(year)
    print(result)
