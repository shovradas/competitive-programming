#!/bin/python3

import os

""" problem: https://www.hackerrank.com/challenges/caesar-cipher-1 """

__author__ = "Shovra Das"

ORDINAL_UPPER = {chr(65+i):i for i in range(26)}
ORDINAL_LOWER = {chr(97+i):i for i in range(26)}
CHARACTER_UPPER = {i:chr(65+i) for i in range(26)}
CHARACTER_LOWER = {i:chr(97+i) for i in range(26)}

def caesarCipher(s, k):
    cipher = ''
    for c in s:
        if c.isalpha():
            if c.isupper():
                encoded = (ORDINAL_UPPER[c] + k) % 26
                cipher += CHARACTER_UPPER[encoded]
            else:
                encoded = (ORDINAL_LOWER[c] + k) % 26
                cipher += CHARACTER_LOWER[encoded]
        else:
            cipher += c
    return cipher
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    _, s, k = int(input()), input(), int(input())
    result = caesarCipher(s, k)
    fptr.write(result + '\n')
    
    fptr.close()
