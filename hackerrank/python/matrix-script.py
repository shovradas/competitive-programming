# Problem Link: https://www.hackerrank.com/challenges/matrix-script/problem

import re

n, m = map(int, input().split())
matrix = [input() for _ in range(n)]

matrix_decoded = ''
for c in range(m):
    for r in range(n):
        matrix_decoded += matrix[r][c]

pattern = r'(?<=[a-zA-Z0-9])[!@#$%& ]+(?=[a-zA-Z0-9])'
print(re.sub(pattern, ' ', matrix_decoded))
