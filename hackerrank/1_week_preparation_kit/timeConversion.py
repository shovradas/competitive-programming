#!/bin/python3

# https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

import os

def timeConversion(s):
    meridiem = s[8:]
    hour = int(s[0:2])
    hour %= 12
    if meridiem == "PM": hour += 12
    s = str(hour).rjust(2, '0') + s[2:8]
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()
