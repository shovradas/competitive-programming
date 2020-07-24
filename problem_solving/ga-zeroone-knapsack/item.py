
__author__ = 'Shovra Das'

class Item:
    def __init__(self, name, profit, weight):
        self.name = name
        self.profit = profit
        self.weight = weight

    def __repr__(self):
        return self.name