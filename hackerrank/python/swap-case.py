# https://www.hackerrank.com/challenges/swap-case/problem

__author__ = "Shovra Das"

def swap_case(s):
    str_out = ''
    for c in s:
        ascii = ord(c)
        if ascii>64 and ascii<91:
            c = chr(ascii+32)
        elif ascii>96 and ascii<123:
            c = chr(ascii-32)
        str_out += c
    return str_out

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)