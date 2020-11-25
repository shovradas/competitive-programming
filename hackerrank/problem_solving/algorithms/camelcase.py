#!/bin/python3

""" problem: https://www.hackerrank.com/challenges/camelcase """

__author__ = "Shovra Das"

def camelcase(s):
    count = 1
    for c in s:
        if 64<ord(c)<91:
            count += 1    
    return count
        
if __name__ == '__main__':
    s = input()
    result = camelcase(s)
    print(result)