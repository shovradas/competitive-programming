# Problem Link: https://www.hackerrank.com/challenges/validating-uid/problem

import re

__author__ = "Shovra Das"

n = int(input())

patterns = {
    re.compile(r'^(.*[A-Z]){2}.*$'),
    re.compile(r'^(.*[0-9]){3}.*$'),
    re.compile(r'[a-zA-Z0-9]'),
    re.compile(r'^(?:([a-zA-Z0-9])(?!.*\1))*$'),
    re.compile(r'^.{10}$')
}

for _ in range(n):
    uid = input()
    match = all(map(lambda pattern: pattern.search(uid), patterns))
    print('Valid' if match else 'Invalid')