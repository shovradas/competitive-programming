# Problem Link: https://www.hackerrank.com/challenges/exceptions/problem

__author__ = "Shovra Das"

t = int(input())

for i in range(t):
    a, b = input().split(' ')    
    try:
        a = int(a)
        b = int(b)
        print(a//b)
    except ValueError as e:
        print(f'Error Code: {e}')
    except ZeroDivisionError as e:
        print(f'Error Code: {e}')