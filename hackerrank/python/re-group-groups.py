# Problem Link: https://www.hackerrank.com/challenges/re-group-groups/problem

import re

string = input()
pattern = re.compile(r'([a-zA-Z0-9])\1+')
match = pattern.search(string)
print(match.group(1) if match else -1)
