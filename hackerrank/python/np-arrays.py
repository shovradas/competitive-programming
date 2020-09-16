# Problem Link: https://www.hackerrank.com/challenges/np-arrays/problem

import numpy

def arrays(arr):
    narr = numpy.array(arr, float)
    return narr[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)