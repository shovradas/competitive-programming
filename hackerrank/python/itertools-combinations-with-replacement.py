# Problem Link: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

# Sample Input
# -------------
# HACK 2

# Sample Output
# -------------
# AA
# AC
# AH
# AK
# CC
# CH
# CK
# HH
# HK
# KK

from itertools import combinations_with_replacement
import os

string, r = input().split()
cmbs = list(combinations_with_replacement(sorted(string), int(r)))
print(*[''.join(c) for c in cmbs], sep=os.linesep)