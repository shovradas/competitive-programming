# Problem Link: https://www.hackerrank.com/challenges/itertools-combinations/problem

import os
from itertools import combinations

string, r = input().split()
for k in range(1, int(r)+1):
    cmbs = list(combinations(''.join(sorted(string)), k))
    print(*[''.join(c) for c in cmbs], sep=os.linesep)