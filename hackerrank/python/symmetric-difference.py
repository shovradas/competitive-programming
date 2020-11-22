# Problem Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

__author__ = "Shovra Das"

input()
a = set(map(int, input().split(' ')))
input()
b = set(map(int, input().split(' ')))

print(*sorted(a.symmetric_difference(b)), sep='\n')