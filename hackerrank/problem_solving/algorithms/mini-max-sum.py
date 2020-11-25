#!/bin/python3

""" problem: https://www.hackerrank.com/challenges/mini-max-sum """

__author__ = "Shovra Das"

def miniMaxSum(arr):
    minimum = maximum = arr[0]
    summation = 0
    for element in arr:
        summation += element
        if element < minimum:
            minimum = element
        if element > maximum:
            maximum = element
    print(summation-maximum, summation-minimum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)