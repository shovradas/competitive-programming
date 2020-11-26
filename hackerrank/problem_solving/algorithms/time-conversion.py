#!/bin/python3

""" problem: https://www.hackerrank.com/challenges/time-conversion """

__author__ = "Shovra Das"

def timeConversion(s):
    pos = s.find(':')
    hour = int(s[:pos])
    
    if s[-2:] == 'AM':
        if hour==12:
            hour = 0
    else:
        if hour!=12:
            hour += 12    
    
    military_time = str(hour).rjust(2, '0') + s[pos:-2]
    
    return military_time
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = timeConversion(s)

    f.write(result + '\n')
    f.close()
