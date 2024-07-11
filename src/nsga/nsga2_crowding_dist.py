import numpy as np

def crowding_distance(population, front):
    """
    Calculate the crowding distance for each solution in the front.
    
    Args:
    - population: list of Individual instances
    - front: list of indices of solutions in the front
    
    Returns:
    - distances: list of crowding distances for each solution in the front
    """
    distances = [0] * len(population)
    front_fitnesses = [population[i].y for i in front]
    num_objectives = len(front_fitnesses[0])
    
    for i in range(num_objectives):
        sorted_front = sorted(front, key=lambda x: population[x].y[i])
        distances[sorted_front[0]] = distances[sorted_front[-1]] = float('inf')
        
        f_max = population[sorted_front[-1]].y[i]
        f_min = population[sorted_front[0]].y[i]
        
        for j in range(1, len(sorted_front) - 1):
            if f_max != f_min:
                distances[sorted_front[j]] += (population[sorted_front[j + 1]].y[i] - population[sorted_front[j - 1]].y[i]) / (f_max - f_min)
    
    return distances
