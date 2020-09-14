# Problem Link: https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import email.utils
import re

n = int(input())

pattern = re.compile(r'^[a-zA-Z][a-zA-Z0-9-_.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$')
for _ in range(n):
    name, email_ = email.utils.parseaddr(input())
    match = pattern.match(email_)
    if match:
        print(email.utils.formataddr((name, email_)))
