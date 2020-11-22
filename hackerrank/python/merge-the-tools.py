# Problem Link: https://www.hackerrank.com/challenges/merge-the-tools/problem


from collections import OrderedDict

__author__ = "Shovra Das"

def merge_the_tools(string, k):   
    for i in range(0, len(string), k):
        ti = string[i:i+k]
        ui = ''.join(OrderedDict.fromkeys(ti))
        print(ui)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)