"""Provides a sample implementation of Binary Search Tree"""

from collections import deque

__author__ = "Shovra Das"

class Node():
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self._root = None

    def insert(self, item):
        node = Node(item)

        if self._root == None:
            self._root = node
        else:
            curr = self._root
            while(True):                
                if curr.item == node.item:
                    raise Exception('BST: Duplicate key found')
                elif node.item>curr.item:
                    if curr.right is None:
                        curr.right = node
                        break
                    curr = curr.right
                else:
                    if curr.left is None:
                        curr.left = node
                        break        
                    curr = curr.left

    def search(self, key):
        stack = deque()
        curr = self._root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()            
            if curr.item == key:
                return curr
            curr = curr.right
        return None

    def inorder(self):
        stack = deque()
        curr = self._root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            print(curr.item, end=' ')
            curr = curr.right

if __name__ == '__main__':
    # Sample implementation
    bst = BST()

    # Insertion
    keys = [50, 10, 30, 45, 65, 25, 15, 85, 70]
    for k in keys:
        bst.insert(k)

    # Print inorder
    bst.inorder()
    print()

    # Search key
    node = bst.search(25)
    if node is not None:
        print(node.item)
    else:
        print('Not found')