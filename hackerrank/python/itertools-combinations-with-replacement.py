# Problem Link: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement
import os

__author__ = "Shovra Das"

string, r = input().split()
cmbs = list(combinations_with_replacement(sorted(string), int(r)))
print(*[''.join(c) for c in cmbs], sep=os.linesep)