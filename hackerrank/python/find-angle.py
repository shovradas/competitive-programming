# Problem Link: https://www.hackerrank.com/challenges/find-angle/problem

__author__ = "Shovra Das"

import math

ab = float(input())
bc = float(input())

theta = math.atan2(ab, bc)  # in radian
theta = math.degrees(theta)

print(f'{int(round(theta, 0))}°')
