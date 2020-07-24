import matplotlib.pyplot as plt
from item import Item
from zeroone_knapsack import ZeroOneKnapsack

__author__ = 'Shovra Das'

def main():
    # Problem ------------------
    items = [
        Item("A", 5, 2),
        Item("B", 15, 4),
        Item("C", 25, 3),
        Item("D", 50, 1),
        Item("E", 60, 1),
        Item("F", 70, 1),
        Item("G", 45, 1)
    ]
    capacity = 10
    # GA Configurations    
    gen_count = int(input("Number of RUN: ") or 5)
    init_pop_size = int(input("Population size: ") or 100)
    elite_size = int(input("Elite size: ") or 50)
    # Run GA
    ks = ZeroOneKnapsack(items, capacity, init_pop_size, elite_size, gen_count)
    ks.ga()    
    maximas = ks.maximas
    print(f'Max profit: {max(maximas, key=lambda x: x[1])[1]}')

    # Plot MaxProfit by Generation
    xData = range(gen_count+1)
    yData = [x[1] for x in maximas]
    
    plt.plot(xData, yData, '-ro')
    for i in range(len(xData)):
        plt.annotate(xy=[xData[i]+0.1,yData[i]], s=f"{yData[i]}")
    plt.ylabel('Profit')
    plt.xlabel('Generations')
    plt.show()

    
if __name__ == '__main__':
    main()