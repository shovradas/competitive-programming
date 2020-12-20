#!/bin/python3

import math
import os
import random
import re

""" problem: https://www.hackerrank.com/challenges/30-binary-numbers """

__author__ = "Shovra Das"

if __name__ == '__main__':
    n = int(input())

    binary_str = ''
    while(n!=0):
        binary_str += str(n%2)
        n = n//2
    
    con1s_list = binary_str.split('0')
    print(max([len(x) for x in con1s_list]))
