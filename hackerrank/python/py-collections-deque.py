# https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque

__author__ = "Shovra Das"

n = int(input().strip())
d = deque()

for i in range(n):
    cmd = input().strip().split(' ')

    if cmd[0] == 'append':
        d.append(cmd[1])
    elif  cmd[0] == 'appendleft':
        d.appendleft(cmd[1])
    elif  cmd[0] == 'pop':
        d.pop()
    else: #  cmd[0] == 'popleft'
        d.popleft()

for i in d:
    print(i, end=' ')
