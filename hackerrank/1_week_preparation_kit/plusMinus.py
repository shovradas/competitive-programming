#!/bin/python3

# https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

def plusMinus(arr):
    n = len(arr)
    assert n>0
    assert n<=100
    
    pos, neg, zero = 0, 0, 0
    for elem in arr:
        assert elem>=-100
        assert elem<=100
        if elem>0: pos+=1
        elif elem<0: neg+=1
        else: zero+=1
    
    print(f"{(pos/n):0.6f}", f"{(neg/n):0.6f}", f"{(zero/n):0.6f}", sep='\n')

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
