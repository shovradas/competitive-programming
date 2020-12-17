#!/bin/python3

""" problem: https://www.hackerrank.com/challenges/hackerrank-in-a-string """

__author__ = "Shovra Das"

def hackerrankInString(string):
    queue = list('hackerrank')

    for char in string:
        if char == queue[0]:
            del queue[0]
        
        if len(queue) == 0:
            return 'YES'
    
    return 'NO'

    
if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()
        result = hackerrankInString(s)
        print(result)