class Stack():
    def __init__(self, size=1024):
        self.size = size
        self.items = [None for x in range(size)]
        self.top = -1

    def empty(self):
        return True if self.top==-1 else False

    def full(self):
        return True if self.top==self.size-1 else False

    def push(self, item):
        if self.full():
            raise Exception('Stack is full!')            

        self.top += 1
        self.items[self.top] = item

    def pop(self):
        if self.empty():
            raise Exception('Stack is empty!')

        item = self.items[self.top]
        self.top -= 1
        return item

    def peek(self):
        return self.items[self.top]    

    def size(self):
        return self.top+1


if __name__ == '__main__':
    # Sample implementation
    stack = Stack(2)
    stack.push(10)
    stack.push(20)
    # stack.push(30) # raises stack full error
    while not stack.empty():
        print(stack.pop())
    # stack.pop() # raises stack empty error