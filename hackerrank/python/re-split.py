# Problem Link: https://www.hackerrank.com/challenges/re-split/problem

import re

__author__ = "Shovra Das"

regex_pattern = r"[.,]"	# Do not delete 'r'.
print("\n".join(re.split(regex_pattern, input())))