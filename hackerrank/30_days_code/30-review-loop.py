""" problem: https://www.hackerrank.com/challenges/30-review-loop """

__author__ = "Shovra Das"

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())

for i in range(n):
    str_in = input().strip()
    str_out_even = ''
    str_out_odd = ''
    for i in range(len(str_in)):
        if i&1 == 0:
            str_out_even += str_in[i]
        else:
            str_out_odd += str_in[i]
    print(str_out_even, str_out_odd)
