# Problem Link: https://www.hackerrank.com/challenges/np-linear-algebra/problem

import numpy

n = int(input())
array = numpy.array([input().split() for _ in range(n)], float)

print(round(numpy.linalg.det(array), 2))