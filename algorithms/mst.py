"""
A sample implentatiobn of Prim's Minimum Spanning Tree algorithm
"""

from queue import SimpleQueue
import random

__author__ = 'Shovra Das'

class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

# Undirected weighted graph, G=(V, E)
class Graph:
    def __init__(self, vertices, edges):
        self._vertices = vertices
        self._edges = edges
        self._graph = None

        self._build_graph()

    def _build_graph(self):
        self._graph = {v: [] for v in self._vertices}
        for edge in self._edges:
            u, v = edge.u
            self._graph[edge.u].append(edge.v)
            self._graph[v].append(u)

    def get_vertices(self):
        return self._vertices

    def get_edges(self):
        return self._edges

    def get_adjacents(self, u):
        return self._graph[u]

    def __repr__(self):
        graph_str = ''
        for vertex in self._graph: 
            graph_str += f'{vertex}->[{",".join(self._graph[vertex])}]\r\n'
        return graph_str.strip()


def MST(graph, start=None):
    if not start:
        start = random.choice(list(graph.get_vertices()))
        print(start)


if __name__ == '__main__':
    # Sample undirected graph
    vertices = {'A', 'B', 'C', 'D', 'E'}
    edges = {
        Edge('A', 'B', 4),
        Edge('A', 'C', 5),
        Edge('B', 'C', 7),
        Edge('B', 'D', 1),
        Edge('C', 'D', 3)
    }
    graph = Graph(vertices, edges)    
    print(graph)

    MST(graph)