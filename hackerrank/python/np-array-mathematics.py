# Problem Link: https://www.hackerrank.com/challenges/np-array-mathematics/problem

import numpy, os

n, m = map(int, input().split())

a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)

print(a+b, a-b, a*b, a//b, a%b, a**b, sep=os.linesep)