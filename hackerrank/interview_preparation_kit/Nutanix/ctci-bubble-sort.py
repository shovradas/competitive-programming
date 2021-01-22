#!/bin/python3

""" problem: https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=nutanix """

__author__ = "Shovra Das"

def countSwaps(a):
    n = len(a)
    swap_count = 0
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j+1], a[j]  #swap(a[j], a[j + 1]);
                swap_count += 1
                
    print(f'Array is sorted in {swap_count} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)
