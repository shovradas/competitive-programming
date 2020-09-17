# Problem Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

n = int(input())

pattern = re.compile(r'^[7-9][0-9]{9}$')
for _ in range(n):
    phone_number = input()
    match = pattern.match(phone_number)
    if match:
        print('YES')
    else:
        print('NO')