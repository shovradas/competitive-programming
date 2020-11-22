# Problem Link: https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy

__author__ = "Shovra Das"

np_array = numpy.array(input().split(), int)
np_2d_array = numpy.reshape(np_array, (3,3))

print(np_2d_array)