""" problem: https://www.hackerrank.com/challenges/30-dictionaries-and-maps """

__author__ = "Shovra Das"

n = int(input().strip())

phone_book = {}
for i in range(n):
    query = input().strip().split(' ')
    phone_book[query[0]] = query[1]

while True:
    try:
        name = input()
    except EOFError:
        break
    if name in phone_book.keys():
        print(f'{name}={phone_book[name]}')
    else:
        print('Not found')
