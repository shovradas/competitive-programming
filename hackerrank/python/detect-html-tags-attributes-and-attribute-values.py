# Problem Link: https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem


import re

n = int(input())
html = ''.join([input() for _ in range(n)])

html = re.sub(r'<!--.*?-->', '', html)

pattern_tag = re.compile(r'<(?!\/|!--).+?>')
pattern_attr = re.compile(r'(\S+)\s*=\s*"([^"]+)')
for tag in pattern_tag.findall(html):
    print(tag.split()[0].strip('<>'))
    for k, v in pattern_attr.findall(tag):
        print(f'-> {k} > {v}')