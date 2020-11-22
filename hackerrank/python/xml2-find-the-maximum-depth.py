# Problem Link: https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem

__author__ = "Shovra Das"


import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # print(elem, maxdepth, level)
    if maxdepth == level:
        maxdepth += 1
    for child in elem:
        depth(child, level+1)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)