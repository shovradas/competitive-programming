# Problem Link: https://www.hackerrank.com/challenges/introduction-to-regex/problem

import re

__author__ = "Shovra Das"

t = int(input())

pattern = re.compile(r"^[+-]?[0-9]*\.[0-9]+$")
for _ in range(t):
    string = input()
    print(bool(re.match(pattern, string)))
