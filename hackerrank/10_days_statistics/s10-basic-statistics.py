# https://www.hackerrank.com/challenges/s10-basic-statistics/problem

from collections import Counter

n, x = int(input()), list(map(int, input().split()))

mean = sum(x)/n

x = sorted(x)
median = x[n>>1] if n&1 == 1 else (x[(n>>1)-1]+x[n>>1])/2

item_frequency = sorted(Counter(x).items())
mode = sorted(item_frequency, key=lambda x: x[1], reverse=True)[0][0]

print(round(mean, 1), round(median, 1), mode, sep='\n')