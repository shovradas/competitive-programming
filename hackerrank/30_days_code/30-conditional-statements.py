#!/bin/python3

import math
import os
import random
import re
import sys

""" problem: https://www.hackerrank.com/challenges/30-conditional-statements """

__author__ = "Shovra Das"

if __name__ == '__main__':
    N = int(input())

    if N&1 == 1:
        print("Weird")
    else:
        if N>1 and N<6:
            print("Not Weird")
        
        elif N>5 and N<21:
            print("Weird")

        else:
           print("Not Weird") 
