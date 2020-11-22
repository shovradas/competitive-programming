# Problem Link: https://www.hackerrank.com/challenges/html-parser-part-1/problem

from html.parser import HTMLParser

__author__ = "Shovra Das"

class MyHTMLParser(HTMLParser):
    def print_attrs_if_any(self, attrs):
        if attrs:
            for k, v in attrs:
                print(f'-> {k} > {v}')

    def handle_starttag(self, tag, attrs):
        print(f'Start : {tag}')
        self.print_attrs_if_any(attrs)

    def handle_endtag(self, tag):
        print(f'End   : {tag}')

    def handle_startendtag(self, tag, attrs):
        print(f'Empty : {tag}')
        self.print_attrs_if_any(attrs)


n = int(input())
parser = MyHTMLParser()
parser.feed(''.join([input() for _ in range(n)]))