#!/bin/python3

import math
import os
import random
import re
import sys

""" problem: https://www.hackerrank.com/challenges/30-loops """

__author__ = "Shovra Das"

if __name__ == '__main__':
    n = int(input())

    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
