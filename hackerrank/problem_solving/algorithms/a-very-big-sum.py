#!/bin/python3
import os

""" problem: https://www.hackerrank.com/challenges/a-very-big-sum """

__author__ = "Shovra Das"

def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    fptr.write(str(result) + '\n')

    fptr.close()
