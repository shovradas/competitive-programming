"""Provides a sample implementation of Linked Stack"""

__author__ = "Shovra Das"

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack():
    def __init__(self):
        self._head = None
        self._count = 0

    def empty(self):
        return True if self._head==None else False

    def push(self, item):
        node = Node(item)
        if not self.empty():            
            node.next = self._head
        self._head = node
        self._count += 1

    def pop(self):
        if self.empty():
            raise Exception('Stack is empty!')
        item = self._head.item
        self._head = self._head.next
        self._count -= 1
        return item

    def peek(self):
        if self.empty():
            raise Exception('Stack is empty!')
        return self._head.item

    def size(self):        
        return self._count


if __name__ == '__main__':
    # Sample implementation
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    
    while not stack.empty():
       print(stack.size(), stack.pop())
    print(stack.size())
    # stack.pop() # raises stack empty error