# Problem Link: https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import os, numpy as np

__author__ = "Shovra Das"

n, m = map(int, input().split())
array = np.array([input().split() for _ in range(n)], int)

np.set_printoptions(legacy='1.13')
print(np.mean(array, axis=1), np.var(array, axis=0), np.std(array), sep=os.linesep)