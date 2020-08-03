"""
A sample implentatiobn of Prim's Minimum Spanning Tree algorithm
"""

from queue import SimpleQueue
import random

__author__ = 'Shovra Das'

# Represents an weighted edge
class WeightedEdge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

class WeightedVertex:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

    def __repr__(self):
        return f'{self.vertex}:{self.weight}'

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
            self._graph[edge.u].append(WeightedVertex(edge.v, edge.weight))
            self._graph[edge.v].append(WeightedVertex(edge.u, edge.weight))

    def get_vertices(self):
        return self._vertices

    def get_edges(self):
        return self._edges

    def get_adjacents(self, u):
        return self._graph[u]

    def __repr__(self):
        graph_str = ''
        for vertex, adjacents in self._graph.items():        
            graph_str += f'{vertex}->[{",".join(map(str, adjacents))}]\r\n'
        return graph_str.strip()


def MST(graph, start=None):
    if not start:
        start = random.choice(list(graph.get_vertices()))
        print(start)


if __name__ == '__main__':
    # Sample undirected graph
    vertices = {'A', 'B', 'C', 'D', 'E'}
    edges = {
        WeightedEdge('A', 'B', 4),
        WeightedEdge('A', 'C', 5),
        WeightedEdge('B', 'C', 7),
        WeightedEdge('B', 'D', 1),
        WeightedEdge('C', 'D', 3)
    }
    graph = Graph(vertices, edges)
    print(graph)

    MST(graph)