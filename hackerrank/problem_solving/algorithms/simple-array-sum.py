#!/bin/python3

import os

""" problem: https://www.hackerrank.com/challenges/simple-array-sum """

__author__ = "Shovra Das"

def simpleArraySum(ar, ar_count):
    sum_ = 0
    for i in range(ar_count):
        sum_ += ar[i]
    return sum_

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar, ar_count)
    fptr.write(str(result) + '\n')

    fptr.close()
