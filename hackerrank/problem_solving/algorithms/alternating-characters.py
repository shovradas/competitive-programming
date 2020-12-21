#!/bin/python3

""" problem: https://www.hackerrank.com/challenges/alternating-characters """

__author__ = "Shovra Das"

def alternatingCharacters(s):
    count = 0
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            count += 1
    return count
    
if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        s = input()
        result = alternatingCharacters(s)
        print(result)