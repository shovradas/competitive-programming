# Problem Link: https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy

__author__ = "Shovra Das"

n, m, p = map(int, input().split())

array_1 = numpy.array([input().split() for _ in range(n)], int)
array_2 = numpy.array([input().split() for _ in range(m)], int)

concatenated = numpy.concatenate((array_1, array_2))

print(concatenated)