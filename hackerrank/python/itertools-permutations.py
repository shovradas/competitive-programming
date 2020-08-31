# Problem Link: https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

string, k = input().split()
for item in permutations(sorted(string), int(k)):
    print(''.join(item))