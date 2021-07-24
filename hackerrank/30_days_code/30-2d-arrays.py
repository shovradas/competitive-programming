#!/bin/python3

""" problem: https://www.hackerrank.com/challenges/30-2d-arrays """

__author__ = "Shovra Das"


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    max_sum = -64
    for i in range(4):
        for j in range(4):
            sum_hg = arr[i][j] + arr[i][j+1] + arr[i][j+2] + \
                  arr[i+1][j+1] + \
                  arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            if max_sum < sum_hg:
                max_sum = sum_hg
    print(max_sum)