# Problem Link: https://www.hackerrank.com/challenges/xml-1-find-the-score/problem


import xml.etree.ElementTree as etree

def get_attr_number(node):
    return sum([len(n.attrib) for n in node.iter()])

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))