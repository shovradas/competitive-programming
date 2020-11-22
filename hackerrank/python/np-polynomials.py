# Problem Link: https://www.hackerrank.com/challenges/np-polynomials/problem

import numpy

__author__ = "Shovra Das"

array = numpy.array(input().split(), float)
x = float(input())

print(numpy.polyval(array, x))
