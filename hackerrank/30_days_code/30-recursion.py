#!/bin/python3

import math
import os
import random
import re
import sys

""" problem: https://www.hackerrank.com/challenges/30-recursion """

__author__ = "Shovra Das"

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
