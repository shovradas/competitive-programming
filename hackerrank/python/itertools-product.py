# Problem Link: https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*product(a, b))