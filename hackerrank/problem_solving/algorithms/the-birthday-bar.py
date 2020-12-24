#!/bin/python3

""" problem: https://www.hackerrank.com/challenges/the-birthday-bar """

__author__ = "Shovra Das"

def birthday(s, d, m):
    count = 0
    for i in range(len(s)-m+1):
        if sum(s[i:i+m])==d:
            count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    s = list(map(int, input().split()))
    d, m = map(int, input().split())
    
    result = birthday(s, d, m)
    print(result)