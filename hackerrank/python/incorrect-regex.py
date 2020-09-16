# Problem Link: https://www.hackerrank.com/challenges/incorrect-regex/problem

import re

t = int(input())
for _ in range(t):
    try:
        re.compile(input())
        print(True)
    except re.error:
        print(False)