# Problem Link: https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy

n, m = map(int, input().split())
array = numpy.array([input().split() for _ in range(n)], int)

sum_ = numpy.sum(array, axis = 0)
print(numpy.prod(sum_))