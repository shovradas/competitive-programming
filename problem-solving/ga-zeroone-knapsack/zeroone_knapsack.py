import random
import operator

__author__ = 'Shovra Das'

class ZeroOneKnapsack:  
    def __init__(self, items, capacity, init_pop_size, elite_size, gen_count):
        self._ITEMS = items
        self._CAPACITY = capacity
        self._CHROMOSOME_SIZE = len(items)
        self._INIT_POP_SIZE = init_pop_size
        self._ELITE_SIZE = elite_size
        self._GEN_COUNT = gen_count

        self._population = []
        self._fitnesses = {}
        self.maximas=[]

    def fitness(self, individual):
        totalWeight = sum([gene*item.weight for gene,item in zip(individual, self._ITEMS)])
        totalProfit = sum([gene*item.profit*item.weight for gene,item in zip(individual, self._ITEMS)])
        
        fitness = totalProfit if totalWeight<=self._CAPACITY else -1
        
        return fitness

    def evaluate(self):
        self._fitnesses = {}
        for i, individual in enumerate(self._population):
            self._fitnesses[i] = self.fitness(individual)

    def select(self):
        fitnesses = sorted(self._fitnesses.items(), key=lambda x:x[1], reverse=True)
        selected = []
        for i in range(self._ELITE_SIZE):
            index = fitnesses[i][0]
            selected.append(self._population[index])
        
        self._population = selected

    def crossover(self, individual1, individual2):
        xPoint = random.randint(1, self._CHROMOSOME_SIZE-1) # One Point Crossover
        
        offspring1 = individual1[:xPoint]
        offspring1.extend(individual2[xPoint:])

        offspring2 = individual2[:xPoint]
        offspring2.extend(individual1[xPoint:])

        return offspring1, offspring2

    def mutation(self, individual):
        for i in range(self._CHROMOSOME_SIZE):
            k = random.random()
            if k>0.5:
                individual[i] = 0 if individual[i]==1 else 1

        return individual

    def initialize_population(self):
        for _ in range(self._INIT_POP_SIZE):
            individual = [random.randint(0, 1) for x in range(self._CHROMOSOME_SIZE)]
            self._population.append(individual)
        
        # Test
        # self._population = [[1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 1]]

    def collect_maximas(self):
        max_fitness = max(self._fitnesses.items(), key=lambda x: x[1])
        index, fitness_value = max_fitness
        self.maximas.append([self._population[index], fitness_value])

    def ga(self):
        self.initialize_population()
        self.evaluate()
        self.collect_maximas()
        for _ in range(self._GEN_COUNT):
            self.select()
            ###################################################################
            # TODO: randomizing selected population to create the mating pool #
            ###################################################################
            new_population = []
            for i in range(len(self._population)):
                individual1 = self._population[i-1]
                individual2 = self._population[i]
                offspring1, offspring2 = self.crossover(individual1, individual2) # applying crossover
                new_population.append(offspring1)
                new_population.append(offspring2)

            for i in range(len(new_population)):
                new_population[i] = self.mutation(new_population[i]) #mutating

            self._population = new_population
            self.evaluate()
            self.collect_maximas()