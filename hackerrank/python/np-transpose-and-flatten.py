# Problem Link: https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy

n, m = map(int, input().split())
lst = [input().split() for _ in range(n)]

np_nd_array = numpy.array(lst, int)
print(numpy.transpose(np_nd_array))
print(np_nd_array.flatten())