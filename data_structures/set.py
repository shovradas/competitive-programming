class Set:
    def __init__(self):
        self.__items = []
    
    def add(self, item):
        if item not in self.__items:
            self.__items.append(item)

    def remove(self, item):
        if item in self.__items:
            self.__items.remove(item)

    def __str__(self) -> str:
        return ', '.join(map(str, self.__items))

if __name__ == '__main__':
    set = Set()
    set.add(10)
    set.add(10)
    set.add(20)

    set.remove(10)

    print(set)