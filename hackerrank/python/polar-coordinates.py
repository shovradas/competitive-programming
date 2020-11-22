# Problem Link: https://www.hackerrank.com/challenges/polar-coordinates/problem

import cmath, os

__author__ = "Shovra Das"

c_number = complex(input())
print(*cmath.polar(c_number), sep=os.linesep)