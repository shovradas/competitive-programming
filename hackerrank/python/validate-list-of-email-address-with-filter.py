# Problem Link: https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

import re

pattern = re.compile(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+[.].{1,3}$')

def fun(s):
    return bool(pattern.match(s))

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)