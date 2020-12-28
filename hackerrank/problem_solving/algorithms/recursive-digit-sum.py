#!/bin/python3

""" problem: https://www.hackerrank.com/challenges/recursive-digit-sum """

__author__ = "Shovra Das"

def superDigit(number, k=1):
    if len(number) == 1:
        return number
    return superDigit(str(sum(map(int, number))*k))

if __name__ == '__main__':
    n, k = input().split()

    result = superDigit(n, int(k))
    print(result)
