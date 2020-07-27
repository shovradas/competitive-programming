"""
Sample implementation of a directed graph data structure
"""

from collections import defaultdict

__author__ = "Shovra Das"

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

class Graph():
    def __init__(self):
        # self._V = defaultdict(lambda: None)
        self._V = {}

    def add_edge(self, src_item, dest_item):
        dest = Node(dest_item)
        if src_item not in self._V:
            self._V[src_item] = None
        dest.next = self._V[src_item]
        self._V[src_item] = dest

    def adj_list(self):
        for k, v in self._V.items():
            print(k, end='')
            curr = v
            while curr:
                print(f'->{curr.item}', end='')
                curr = curr.next
            print()

if __name__ == '__main__':
    # V = ['A', 'B', 'C', 'D']
    # E = ['A-B', 'A-C', 'B-C', 'B-D', 'C-D']
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'D')
    graph.adj_list()
