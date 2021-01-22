#!/bin/python3

""" problem: https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=arcesium """

__author__ = "Shovra Das"

from collections import Counter

def check_magazine(magazine, note):
    return (Counter(note) - Counter(magazine)) == {}

if __name__ == '__main__':
    m, n = map(int, input().split())

    magazine = input().rstrip().split()
    note = input().rstrip().split()
    
    print('Yes' if check_magazine(magazine, note) else 'No')