# Problem Link: https://www.hackerrank.com/challenges/validating-credit-card-number/problem

import re

__author__ = "Shovra Das"

pattern = re.compile(r'^[4-6]\d{3}(-?\d{4}){3}$')
pattern_repeat = re.compile(r'(\d)\1{3}')

n = int(input())
for _ in range(n):
    cc = input()
    match = pattern.match(cc)
    if match:
        cc = re.sub(r'-', '', match.group())
        match = pattern_repeat.search(cc)
        print('Invalid' if match else 'Valid')
    else:
        print('Invalid')
