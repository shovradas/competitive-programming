#!/bin/python3

""" problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records """

__author__ = "Shovra Das"

def breakingRecords(scores):
    highest = lowest = scores[0]
    highest_count = lowest_count = 0
    for score in scores[1:]:
        if score < lowest:
            lowest = score
            lowest_count += 1
        elif score > highest:
            highest = score
            highest_count += 1
            
    return highest_count, lowest_count
        

if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    print(' '.join(map(str, result)))