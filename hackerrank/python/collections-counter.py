# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

__author__ = "Shovra Das"

x = int(input().strip())
shoe_sizes = input().strip().split(' ')
n = int(input().strip())

shoe_sizes = Counter(shoe_sizes)
earned_amount = 0
for i in range(n):
    desired = input().strip().split(' ')
    size = desired[0]
    amount = int(desired[1])
    if size in shoe_sizes and shoe_sizes[size] > 0:
        earned_amount += amount
        shoe_sizes[size] -= 1

print(earned_amount)
