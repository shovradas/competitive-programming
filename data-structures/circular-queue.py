"""Provides a sample implementation of Circular Queue"""

__author__ = "Shovra Das"

class Queue():
    def __init__(self, size=1024):
        self._items = [None for x in range(size)]
        self._front = 0
        self._rear = 0
        self._count = 0

    def empty(self):
        return True if self._count==0 else False

    def full(self):
        return True if self._count==len(self._items) else False

    def push(self, item):
        if self.full():
            raise Exception('Queue is full!')
        
        self._items[self._rear] = item        
        self._rear += 1
        self._count += 1

        # for circular
        if self._rear == len(self._items):
            self._rear = 0

    def pop(self):
        if self.empty():
            raise Exception('Queue is empty!')

        item = self._items[self._front]
        self._front += 1
        self._count -= 1

        # for circular
        if self._front == len(self._items):
            self._front = 0

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
        return self._count


if __name__ == '__main__':
    # Sample implementation
    queue = Queue(4)
    queue.push(10)
    queue.push(20)
    queue.push(30)
    queue.push(40)
    # queue.push(50)  # raises queue full error

    # print(queue.size(), queue.front(), queue.back(), queue.pop())
    # print(queue.size(), queue.front(), queue.back(), queue.pop())    
    # queue.push(60)
    # print(queue.size(), queue.front(), queue.back())
    # queue.push(70)
    # print(queue.size(), queue.front(), queue.back())
    # queue.push(80) # raises queue full error
    
    while not queue.empty():
       print(queue.size(), queue.pop())
    print(queue.size())
    queue.pop()  # raises queue empty error