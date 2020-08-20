# Problem Link: https://www.hackerrank.com/challenges/designer-door-mat/problem

n, m = list(map(int, input().split(' ')))
format_char = '.|.'

for i in range(1, n, 2):
    print((format_char*i).center(m, '-'))

print("WELCOME".center(m, '-'))

for i in range(n-2, 0, -2):
    print((format_char*i).center(m, '-'))