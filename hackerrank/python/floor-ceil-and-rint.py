# Problem Link: https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

import numpy, os

a = numpy.array(input().split(), float)
numpy.set_printoptions(legacy='1.13') # Added to match output with extra space
print(numpy.floor(a), numpy.ceil(a), numpy.rint(a), sep=os.linesep)
