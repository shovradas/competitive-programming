# Problem Link: https://www.hackerrank.com/challenges/python-time-delta/problem

__author__ = "Shovra Das"

import math
import os
import random
import re
import sys
from datetime import datetime

def time_delta(t1, t2):
    t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    time_delta = t1-t2
    return abs(time_delta.total_seconds())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)
        fptr.write(str(int(delta)) + '\n')
    fptr.close()
