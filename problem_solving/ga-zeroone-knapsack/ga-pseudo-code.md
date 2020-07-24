### The Canonical GA Pseudo code

```
choose initial population
evaluate each individual's fitness
determine population's average fitness
repeat
        select best-ranking individuals to reproduce
        mate pairs at random
        apply crossover operator
        apply mutation operator
        evaluate each individual's fitness
        determine population's average fitness
until terminating condition (e.g. until at least one individual has the desired fitness or enough generations have passed)
```

[Source](https://wiki.c2.com/?GeneticAlgorithm)