# Problem Link: https://www.hackerrank.com/challenges/html-parser-part-2/problem

from html.parser import HTMLParser

__author__ = "Shovra Das"

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if data.strip():
            comment_type = 'Multi' if '\n' in data else 'Single'
            print(f'>>> {comment_type}-line Comment', data, sep='\n')
  
    def handle_data(self, data):
        if data.strip():
            print('>>> Data', data, sep='\n')


html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
