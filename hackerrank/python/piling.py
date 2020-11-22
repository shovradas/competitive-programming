# Problem Link: https://www.hackerrank.com/challenges/piling-up/problem


import sys
from collections import deque

__author__ = "Shovra Das"

t = int(input())

for _ in range(t):
    _, cubes = input(), deque(map(int, input().split()))

    top = sys.maxsize
    is_stackable = True
    while cubes:        
        if cubes[0] > top or cubes[-1] > top:
            is_stackable = False
            break
        top = cubes.popleft() if cubes[0] > cubes[-1] else cubes.pop()        
    print('Yes' if is_stackable else 'No')
    
