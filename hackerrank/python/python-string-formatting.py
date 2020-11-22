# https://www.hackerrank.com/challenges/python-string-formatting/problem

__author__ = "Shovra Das"


def print_formatted(number):
    w = len('{:b}'.format(number))
    # your code goes here
    for i in range(1, number+1):
        d = '{:d}'.format(i)
        o = '{:o}'.format(i)
        h = '{:X}'.format(i)
        b = '{:b}'.format(i)
        print(d.rjust(w), o.rjust(w), h.rjust(w), b.rjust(w))

        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)