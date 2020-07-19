class Stack():
    def __init__(self, size=1024):
        self._items = [None for x in range(size)]
        self._top = -1

    def empty(self):
        return True if self._top==-1 else False

    def full(self):
        return True if self._top==len(self._items) else False

    def push(self, item):
        if self.full():
            raise Exception('Stack is full!')

        self._top += 1
        self._items[self._top] = item

    def pop(self):
        if self.empty():
            raise Exception('Stack is empty!')

        item = self._items[self._top]
        self._top -= 1
        return item

    def peek(self):
        return self._items[self._top]

    def size(self):
        return self._top+1


if __name__ == '__main__':
    # Sample implementation
    stack = Stack(2)
    stack.push(10)
    stack.push(20)
    # stack.push(30) # raises stack full error
    while not stack.empty():
        print(stack.pop(), stack.size())
    # stack.pop() # raises stack empty error