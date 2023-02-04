#!/bin/python3

# https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one


def miniMaxSum(arr):
    _min, _max, total = 1_000_000_000, 1, 0
    for elem in arr:
        assert elem >= 1
        assert elem <= 1_000_000_000
        if elem < _min: _min = elem
        if elem > _max: _max = elem
        total += elem
    
    print(total-_max, total-_min)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
