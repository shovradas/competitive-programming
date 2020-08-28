# Problem Link: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

n = int(input())

items = OrderedDict()
for i in range(n):
    item_name, _, net_price = input().rpartition(' ')
    if item_name in items:
        items[item_name] += int(net_price)
    else:
        items[item_name] = int(net_price)

for i in items:
    print(i, items[i])
