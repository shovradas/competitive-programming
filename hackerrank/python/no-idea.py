# Problem Link: https://www.hackerrank.com/challenges/no-idea/problem

__author__ = "Shovra Das"

l = lambda: map(int, input().split(' '))

n, m = l()
array = list(l())
a = set(l())
b = set(l())

happiness = 0
for i in array:
    if i in a:
        happiness += 1
    elif i in b:
        happiness -= 1

print(happiness)