class Queue():
    def __init__(self, size=1024):
        self._items = [None for x in range(size)]
        self._front = 0
        self._rear = 0

    def empty(self):
        return True if self._front==self._rear else False

    def full(self):
        return True if self._rear==len(self._items) else False

    def push(self, item):
        if self.full():
            raise Exception('Queue is full!')
        
        self._items[self._rear] = item
        self._rear += 1

    def pop(self):
        if self.empty():
            raise Exception('Queue is empty!')

        item = self._items[self._front]
        self._front += 1
        return item

    def front(self):
        if self.empty():
            raise Exception('Queue is empty!')
        return self._items[self._front]

    def back(self):
        if self.empty():
            raise Exception('Queue is empty!')
        return self._items[self._rear-1]

    def size(self):
        return self._rear - self._front


if __name__ == '__main__':
    # Sample implementation
    queue = Queue(4)
    queue.push(10)
    queue.push(20)
    queue.push(30)
    queue.push(40)

    # print(queue.size(), queue.front(), queue.back(), queue.pop())
    # print(queue.size(), queue.front(), queue.back(), queue.pop())
    # print(queue.size(), queue.front(), queue.back(), queue.pop())
    # print(queue.size(), queue.front(), queue.back(), queue.pop())
    # print(queue.size())
    # print(queue.pop())  # raises queue empty error
    
    while not queue.empty():
       print(queue.size(), queue.pop())
    print(queue.size())
    # queue.pop() # raises queue empty error