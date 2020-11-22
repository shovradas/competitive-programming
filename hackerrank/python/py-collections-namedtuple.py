# Problem Link: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

__author__ = "Shovra Das"

n, Record = int(input()), namedtuple('Record', ','.join(input().split()))
records = [Record(*input().split()) for _ in range(n)]
print(sum([int(record.MARKS) for record in records])/n)