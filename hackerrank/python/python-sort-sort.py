# Problem Link: https://www.hackerrank.com/challenges/python-sort-sort/problem

import os

__author__ = "Shovra Das"


if __name__ == '__main__':
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    k = int(input())

    sorted_data = sorted(data, key=lambda x:x[k])
    for row in sorted_data:
        print(' '.join([str(col) for col in row]))