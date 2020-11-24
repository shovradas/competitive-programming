#!/bin/python3

""" problem: https://www.hackerrank.com/challenges/diagonal-difference """

__author__ = "Shovra Das"

def diagonalDifference(arr):
    diff = 0
    l = len(arr)
    for i in range(l):
        diff += arr[i][i] - arr[i][l-i-1]
    return abs(diff)

if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    result = diagonalDifference(arr)
    print(str(result))