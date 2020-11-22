# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

__author__ = "Shovra Das"


n1 = int(input().strip())
s1 = set(input().strip().split(' '))
n2 = int(input().strip())
s2 = set(input().strip().split(' '))

s3 = s1.symmetric_difference(s2)

print(len(s3))
