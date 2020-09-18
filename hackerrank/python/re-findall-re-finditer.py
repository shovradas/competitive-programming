# Problem Link: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

import re, os

v = 'aeiouAEIOU'
c = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'

string = input()
pattern = re.compile(r'(?<=[%s])[%s]{2,}(?=[%s}])' % (c, v, c))
matches = pattern.findall(string)
if matches:
    print(*matches, sep=os.linesep)
else:
    print(-1)