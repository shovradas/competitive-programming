#!/bin/python3

from functools import reduce

""" problem: https://www.hackerrank.com/challenges/between-two-sets """

__author__ = "Shovra Das"

def gcd(x, y):
    small = x if x<y else y
    g = 1
    for i in range(2, small+1):
        if((x%i == 0) and (y%i == 0)): 
            g = i
    return g

    
def lcm(x, y):
    return x*y//gcd(x, y)

    
def getTotalX(a, b):
    l, g = reduce(lcm, a), reduce(gcd, b)    
    return sum([(g%i)==0 for i in range(l, g+1, l)])


if __name__ == '__main__':
    n, m = input().split()
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    
    print(getTotalX(arr, brr))