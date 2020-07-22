"""Provides a sample implementation of Binary Search Tree"""

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

    def traverse(self):
        curr = self._root
        print(curr.item)
        print(curr.left.item)
        print(curr.right.item)
        print(curr.right.right.item)
        print(curr.left.left.item)
        print(curr.right.left.item)
        print(curr.left.left.left.item)


if __name__ == '__main__':
    # Sample implementation
    bst = BST()
    bst.insert(50)
    bst.insert(60)
    bst.insert(45)
    bst.insert(70)
    bst.insert(40)
    bst.insert(55)
    bst.insert(30)
    bst.traverse()