class Node:
    def __init__(self, item):
        self._item = item
        self._children = []

    def add_child(self, node):
        self._children.append(node)

    def get_item(self):
        return self._item
    
    def get_children(self):
        return self._children


def preorder(node):
    print(node.get_item(), end=' ')    
    for child in node.get_children():
        preorder(child)


if __name__ == '__main__':
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')
    A.add_child(B)
    A.add_child(C)
    B.add_child(D)
    B.add_child(E)

    preorder(A)