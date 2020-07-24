__author__ = 'Shovra Das'

class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness= 0.0

    def routeDistance(self):
        if(self.distance==0):
            for i, city in enumerate(self.route):
                toCity = self.route[i+1] if city != self.route[-1] else self.route[0]
                self.distance += city.distance(toCity)
        return self.distance

    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness

    def __repr__(self):
        return f"{self.route}, {self.distance}, {self.fitness}"