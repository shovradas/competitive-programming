# Problem Link: https://www.hackerrank.com/challenges/np-dot-and-cross/problem

import numpy

__author__ = "Shovra Das"

n = int(input())

a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)

print(numpy.dot(a, b))
