#!/bin/python3

""" problem: https://www.hackerrank.com/challenges/matrix-rotation-algo """

__author__ = "Shovra Das"

def matrixRotation(matrix, m, n, r):
    row, col = m, n
    index_map = {}
    i = 0  # layer number starting from outer
    while(row>0 and col>0):
        # Generating Indexes by layers
        layer = []
        for j in range(i, col+i): 
            layer.append((i, j))
        for j in range(1+i, row+i): 
            layer.append((j, col-1+i))
        if row!=1:
            for j in range(col-2+i, -1+i, -1): 
                layer.append((row-1+i, j))        
        if col!=1:
            for j in range(row-2+i, i, -1): 
                layer.append((j, i))
        
        # Mapping indexes
        l = len(layer)
        for k in range(l): 
            index_map[layer[k]] = layer[(k+r)%l]
           
        row -= 2
        col -= 2        
        i += 1
    
    # Print
    for i in range(m):
        for j in range(n):
            r, c = index_map[(i, j)]
            print(matrix[r][c], end=' ')
        print()
    

if __name__ == '__main__':
    m, n, r = map(int, input().split())
    matrix = [input().split() for _ in range(m)]
    matrixRotation(matrix, m, n, r)
