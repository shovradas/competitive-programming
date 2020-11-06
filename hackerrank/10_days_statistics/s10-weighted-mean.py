# https://www.hackerrank.com/challenges/s10-weighted-mean/problem


n = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))

weighted_mean = sum([xi*wi for xi, wi in zip(x, w)]) / sum(w)
print(round(weighted_mean, 1))