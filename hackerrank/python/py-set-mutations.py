# Problem Link: https://www.hackerrank.com/challenges/py-set-mutations/problem

len_a = int(input())
a = set(map(int, input().split(' ')))
n = int(input())

for i in range(n):
    cmd, len_b = input().split(' ')
    b = set(map(int, input().split(' ')))
    getattr(a, cmd)(b)

print(sum(a))