# import random
from individual import Individual
def recombine(parent1, parent2,random):
    size = len(parent1.g)  # Assuming parent1 and parent2 are lists of elements
    offspring1 = Individual()
    offspring2 = Individual()
    offspring1.g = list()
    offspring2.g = list()

    for i in range(size):
        if random.random() < 0.5:
            offspring1.g.append(parent1.g[i])
            offspring2.g.append(parent2.g[i])
        else:
            offspring1.g.append(parent2.g[i])
            offspring2.g.append(parent1.g[i])

    return offspring1

# # Example usage
# parent1 = ['a', 'b', 'c', 'd']
# parent2 = ['e', 'f', 'a', 'b']
# child1, child2 = uniform_crossover(parent1, parent2)

# print("Child 1:", child1)
# print("Child 2:", child2)
