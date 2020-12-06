#!/bin/python3

""" problem: https://www.hackerrank.com/challenges/apple-and-orange """

__author__ = "Shovra Das"

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = sum([s <= (a+distance) <= t for distance in apples])
    oranges_count = sum([s <= (b+distance) <= t for distance in oranges])
    print(apple_count, oranges_count, sep= '\n')

if __name__ == '__main__':
    s, t = map(int, input().split())    
    a, b = map(int, input().split())
    mn = map(int, input().split())
    apples = list(map(int, input().split()))
    oranges = list(map(int, input().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
