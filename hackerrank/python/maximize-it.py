# Problem Link: https://www.hackerrank.com/challenges/maximize-it/problem

from itertools import product

k, m = map(int, input().split())
n = [list(map(int, input().split()[1:])) for _ in range(k)]

s = lambda list_: sum(x*x for x in list_)%m
print(max(map(s, product(*n))))
