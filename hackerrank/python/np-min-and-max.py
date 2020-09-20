# Problem Link: https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy

n, m = map(int, input().split())
array = numpy.array([input().split() for _ in range(n)], int)
array = numpy.min(array, axis=1)
print(numpy.max(array))