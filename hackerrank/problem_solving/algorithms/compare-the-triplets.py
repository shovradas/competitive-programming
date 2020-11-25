#!/bin/python3

""" problem: https://www.hackerrank.com/challenges/compare-the-triplets """

__author__ = "Shovra Das"

def compareTriplets(a, b):
    score_alice = score_bob = 0
    for sa, sb in zip(a, b):
        if sa == sb:
            continue
        if sa > sb:
            score_alice += 1
        else:
            score_bob += 1
            
    return score_alice, score_bob

if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    
    scores = compareTriplets(a, b)
    print(*scores)