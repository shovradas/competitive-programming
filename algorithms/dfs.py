"""
A sample implentatiobn for Depth First Search (DFS) algorithm
"""

from collections import deque
from collections import defaultdict

__author__ = 'Shovra Das'

class Graph:
    def __init__(self):
        self._V = defaultdict(list)

    def add_edge(self, u, v):
        self._V[u].append(v)

    def get_adjacents(self, u):
        return self._V[u]

    def __repr__(self):
        graph_str = ''
        for vertex in self._V: 
            graph_str += f'{vertex}->[{",".join(self._V[vertex])}]\r\n'
        return graph_str.strip()


def DFS(graph, start, goal=None):
    stack = deque()

    stack.append(start)
    visited = set(start)    
    while stack:
        vertex = stack.pop()
        print(vertex, end=' ')
        if goal and goal==vertex:
            return vertex

        for adj in graph.get_adjacents(vertex):          
            if adj not in visited:
                stack.append(adj)
                visited.add(adj) 
    return None


if __name__ == '__main__':
    # Sample graph
    vertices = ['A', 'B', 'C', 'D']
    edges = ['A-B', 'A-C', 'B-C', 'B-D', 'C-D']

    # Preparing graph
    graph = Graph()
    for edge in edges:
        u, v = edge.split('-')
        graph.add_edge(u, v)
    print(graph)
    
    # No goal specified. Traverses the whole graph
    DFS(graph, 'A')
    print()

    # Goal node specified. Returns the node or None if not found
    vertex = DFS(graph, 'A', 'E')
    if vertex:
        print(f'=> Found: {vertex}')
    else:
        print('=> Not found')