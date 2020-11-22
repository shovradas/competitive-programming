# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem


from statistics import mean

__author__ = "Shovra Das"

def average(array):
    # your code goes here
    distinct_heights = set(array)
    return mean(distinct_heights)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)