# Problem Link: https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from itertools import combinations

n, l, k = int(input()), input().split(), int(input())

combs = list(combinations(l, k))
total_freq = sum([1 for c in combs if 'a' in c])
print(round(total_freq/len(combs), 3))