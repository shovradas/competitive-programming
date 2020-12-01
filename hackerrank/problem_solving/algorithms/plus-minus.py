#!/bin/python3

""" problem: https://www.hackerrank.com/challenges/plus-minus """

__author__ = "Shovra Das"

def plusMinus(arr):
    pos = neg = zero = 0
    for i in arr:
        if i==0: zero += 1
        elif i>0: pos += 1
        else: neg += 1
    n = len(arr)
    print(round(pos/n, 6), round(neg/n, 6), round(zero/n, 6), sep='\n')

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
