import random
import operator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from city import City
from fitness import Fitness

__author__ = 'Shovra Das'

# Create the population ===========================
def createRoute(cityList):
    route = random.sample(cityList, len(cityList))
    return route

def initialPopulation(popSize, cityList):
    population = []
    for i in range(popSize):
        population.append(createRoute(cityList))
    return population
# =================================================

# Evaluation ======================================
def rankRoutes(population):
    fitnessResults = {}
    for i in range(len(population)):
        fitnessResults[i] = Fitness(population[i]).routeFitness()
    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)
# =================================================

# Selection =======================================
def selection(popRanked, eliteSize):
    selectionResults = []
    df = pd.DataFrame(popRanked, columns=["Index","Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()
    #print(df)
    #ut.printList(popRanked)
    
    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0])

    #print(selectionResults)
    
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100*random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i,3]:
                selectionResults.append(popRanked[i][0])
                break

    #print(selectionResults)

    return selectionResults
# =================================================

def matingPool(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])

    #ut.printList(matingpool)
    return matingpool

def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []
    
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])
        
    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    return child

def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0,eliteSize):
        children.append(matingpool[i])
    
    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool)-i-1])
        children.append(child)
    return children

def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))
            
            city1 = individual[swapped]
            city2 = individual[swapWith]
            
            individual[swapped] = city2
            individual[swapWith] = city1
    return individual

def mutatePopulation(population, mutationRate):
    mutatedPop = []
    
    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop

def nextGeneration(currentGen, eliteSize, mutationRate):
    popRanked = rankRoutes(currentGen)
    selectionResults = selection(popRanked, eliteSize)
    matingpool = matingPool(currentGen, selectionResults)
    children = breedPopulation(matingpool, eliteSize)
    nextGeneration = mutatePopulation(children, mutationRate)
    return nextGeneration

def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations):
    pop = initialPopulation(popSize, population)
    print("Initial distance: " + str(1 / rankRoutes(pop)[0][1]))
    
    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)
    
    print("Final distance: " + str(1 / rankRoutes(pop)[0][1]))
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute


# cityList = [
#     City(137,196),
#     City(4,145),
#     City(131,182),
#     City(119,114),
#     City(85,64),
#     City(90,197),
#     City(60,92),
#     City(33,9),
#     City(42,103),
#     City(33,184)
#     # City(36,134),
#     # City(152,129),
#     # City(115,111),
#     # City(157,111),
#     # City(180,50),
#     # City(15,193),
#     # City(43,56),
#     # City(89,90),
#     # City(147,80),
#     # City(65,3),
#     # City(15,26),
#     # City(79,36),
#     # City(16,144),
#     # City(34,27)
# ]


# bestRoute = geneticAlgorithm(population=cityList, popSize=20, eliteSize=5, mutationRate=0.01, generations=5)
# print(bestRoute)
# bestRoute = geneticAlgorithm(population=cityList, popSize=50, eliteSize=5, mutationRate=0.01, generations=10)
# print(bestRoute)

cityList = []
for i in range(0,24):
    cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))

geneticAlgorithm(population=cityList, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)

# cityList = [City(5, 0), City(0, 12), City(5, 12), City(12, 5), City(5, 5)]
# population = initialPopulation(5, cityList)
# ut.printList(population)
# ranked = rankRoutes(population)
# ut.printList(fittests)
# selected = selection(ranked, 3)
# print(selected)
# matingpool = matingPool(population, selected)


def geneticAlgorithmPlot(population, popSize, eliteSize, mutationRate, generations):
    pop = initialPopulation(popSize, population)
    progress = []
    progress.append(1 / rankRoutes(pop)[0][1])
    
    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)
        progress.append(1 / rankRoutes(pop)[0][1])
    
    plt.plot(progress)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.show()

geneticAlgorithmPlot(population=cityList, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)
