# Problem Link: https://www.hackerrank.com/challenges/validating-postalcode/problem


import re

__author__ = "Shovra Das"

regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"([0-9])(?=[0-9]\1)"

P = input()
print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
