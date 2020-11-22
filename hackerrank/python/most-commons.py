# Problem Link: https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter

__author__ = "Shovra Das"

string = sorted(input())
for char_count in Counter(string).most_common(3):
    print(*char_count)