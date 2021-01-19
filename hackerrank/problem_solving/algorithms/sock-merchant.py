#!/bin/python3

from collections import defaultdict

""" problem: https://www.hackerrank.com/challenges/sock-merchant """

__author__ = "Shovra Das"

def sockMerchant(array):
    counts = defaultdict(int)
    pair_count = 0
    for item in array:
        counts[item] += 1
        if counts[item]&1 == 0:
            pair_count += 1
    
    return pair_count
    
if __name__ == '__main__':
    input()
    array = list(map(int, input().split()))
    result = sockMerchant(array)
    print(result)