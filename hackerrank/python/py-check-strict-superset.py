# Problem Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

__author__ = "Shovra Das"

a = set(map(int, input().split(' ')))
n = int(input())

len_a = len(a)
isstrict = True
for i in range(n):
    givenset = set(map(int, input().split(' ')))
    if len(givenset) >= len_a or not givenset.issubset(a):
        isstrict = False
        break
print(isstrict)