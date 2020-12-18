#!/bin/python3

""" problem: https://www.hackerrank.com/challenges/pangrams """

__author__ = "Shovra Das"

def pangrams(s):
    s = set(s.lower())
    return 'pangram' if len(s)==27 else 'not pangram'

if __name__ == '__main__':
    s = input()
    result = pangrams(s)
    print(result)