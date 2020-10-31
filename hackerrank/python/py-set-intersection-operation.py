# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem


n1 = int(input().strip())
s1 = set(input().strip().split(' '))
n2 = int(input().strip())
s2 = set(input().strip().split(' '))

s3 = s1.intersection(s2)

print(len(s3))