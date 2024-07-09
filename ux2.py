# import random
from individual import Individual
def recombine(parent1, parent2,random):
    rows = len(parent1.g)  # Assuming parent1 and parent2 are lists of elements
    columns = len(parent1.g[0])
    offspring1 = Individual()
    offspring2 = Individual()
    offspring1.g = list()
    offspring2.g = list()

    for i in range(rows):
        if random.random() < 0.5:
            offspring1.g.append(parent1.g[i])
            offspring2.g.append(parent2.g[i])
        else:
            offspring1.g.append(parent2.g[i])
            offspring2.g.append(parent1.g[i])

    return offspring1