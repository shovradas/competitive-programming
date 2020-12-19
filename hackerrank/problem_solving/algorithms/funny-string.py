#!/bin/python3

""" problem: https://www.hackerrank.com/challenges/funny-string """

__author__ = "Shovra Das"

def funnyString(s):
    n = len(s)
    for i in range(n-1):
        actual = abs(ord(s[i])-ord(s[i+1]))
        reverse = abs(ord(s[n-i-1])-ord(s[n-i-2]))
        if actual != reverse:
            return 'Not Funny'
    return 'Funny'

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()
        result = funnyString(s)
        print(result)