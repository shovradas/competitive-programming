# Problem Link: https://www.hackerrank.com/challenges/np-inner-and-outer/problem

import numpy, os

__author__ = "Shovra Das"

a = numpy.array(input().split(), int)
b = numpy.array(input().split(), int)

print(numpy.inner(a, b), numpy.outer(a, b), sep=os.linesep)