# Problem Link: https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby

__author__ = "Shovra Das"

string = input()
compressed = [(len(list(g)), int(c)) for c, g in groupby(string)]  # variable name was groups in actual submission
print(*compressed)
