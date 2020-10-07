# Problem Link: https://www.hackerrank.com/challenges/ginorts/problem

string = sorted(input())

lower, upper, odd, even = ['']*4

for char in string:    
    if char.islower():
        lower += char
    elif char.isupper():
        upper += char
    else:
        if int(char) & 1 == 1:
            odd += char
        else:
            even += char

print(lower, upper, odd, even, sep='')