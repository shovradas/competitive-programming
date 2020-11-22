# Problem Link: https://www.hackerrank.com/challenges/python-mod-divmod/problem

__author__ = "Shovra Das"

a = int(input())
b = int(input())
result = divmod(a, b)
print(*result, result, sep='\n')