# Problem Link: https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

import re

n = int(input())

pattern = re.compile(r'(?<= )(&&|\|\|)(?= )')
repl = lambda match: 'and' if match.group() == '&&' else 'or'

for _ in range(n):
    line = input()
    print(re.sub(pattern, repl, line))
