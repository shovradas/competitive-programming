class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue():
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def empty(self):
        return True if self._head==None else False

    def push(self, item):
        node = Node(item)

        if self.empty():
            self._head = node
        else:
            self._tail.next = node

        self._tail = node
        self._count += 1

    def pop(self):
        if self.empty():
            raise Exception('Queue is empty!')
        item = self._head.item
        self._head = self._head.next
        self._count -= 1
        return item

    def front(self):
        if self.empty():
            raise Exception('Queue is empty!')
        return self._head.item

    def back(self):
        if self.empty():
            raise Exception('Queue is empty!')
        return self._tail.item

    def size(self):
        return self._count


if __name__ == '__main__':
    # Sample implementation
    queue = Queue()
    queue.push(10)
    queue.push(20)
    queue.push(30)
    queue.push(40)

    print(queue.size(), queue.front(), queue.back(), queue.pop())
    print(queue.size(), queue.front(), queue.back(), queue.pop())
    print(queue.size(), queue.front(), queue.back(), queue.pop())
    print(queue.size(), queue.front(), queue.back(), queue.pop())
    print(queue.size())
    print(queue.pop())
    
    # while not queue.empty():
    #    print(queue.size(), queue.pop())
    # print(queue.size())
    # queue.pop() # raises stack empty error