#!/bin/python3

from collections import Counter

""" problem: https://www.hackerrank.com/challenges/migratory-birds """

__author__ = "Shovra Das"

def migratoryBirds(arr):
    counts = Counter(arr)
    count_list = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return count_list[0][0]

if __name__ == '__main__':
    _ = input()
    arr = list(map(int, input().split()))

    result = migratoryBirds(arr)
    print(result)