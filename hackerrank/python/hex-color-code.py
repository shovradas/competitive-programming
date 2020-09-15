# Problem Link: https://www.hackerrank.com/challenges/hex-color-code/problem

import re

n = int(input())

pattern = re.compile(r'(#(?:[0-9a-fA-F]{3}){1,2})')
for _ in range(n):
    line = input()
    match = pattern.findall(line, 1)
    if match:
        print(*match, sep='\n')
