#!/bin/python3

""" problem: Multiples of 3 and 5 (https://projecteuler.net/problem=1) """

__author__ = "Shovra Das"

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    n = n-1

    n3 = n//3
    n5 = n//5
    n15 = n//15
    
    sum3 = 3 * (n3*(n3+1)//2)
    sum5 = 5 * (n5*(n5+1)//2)
    sum15 = 15 * (n15*(n15+1)//2)
    
    print(sum3 + sum5 - sum15)