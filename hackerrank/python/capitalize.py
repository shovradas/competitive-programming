# https://www.hackerrank.com/challenges/capitalize/problem


import os


def solve(s):

    ascii = ord(s[0])    
    str_out = chr(ascii-32) if ascii>96 and ascii<123 else s[0]

    for i in range(1, len(s)):
        ascii = ord(s[i])
        if ascii>96 and ascii<123 and s[i-1]==' ':
            ascii = ascii-32
        str_out += chr(ascii)

    return str_out


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
