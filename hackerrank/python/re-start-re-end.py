# Problem Link: https://www.hackerrank.com/challenges/re-start-re-end/problem

import re

s, k = input(), input()

pattern = re.compile(k)
match = pattern.search(s, 0)
if not match:
    print((-1, -1))
else:
    while match:
        print((match.start(), match.end() - 1))
        match = pattern.search(s, match.start() + 1)