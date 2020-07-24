import numpy as np

__author__ = 'Shovra Das'

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, city):
        dx = self.x - city.x
        dy = self.y - city.y
        euclideanDistance = np.sqrt(dx*dx + dy*dy)
        return euclideanDistance

    def __repr__(self):
        return f"({self.x},{self.y})"