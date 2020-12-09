#!/bin/python3

""" problem: https://www.hackerrank.com/challenges/birthday-cake-candles """

__author__ = "Shovra Das"

def birthdayCakeCandles(candles):
    max_height = candles[0]
    count = 1
    for i in range(1, len(candles)):       
        if max_height < candles[i]:
            max_height = candles[i]
            count = 1            
        elif max_height == candles[i]:
            count += 1    
    return count

if __name__ == '__main__':
    candles_count = int(input())
    candles = list(map(int, input().split()))
    result = birthdayCakeCandles(candles)

    print(result)