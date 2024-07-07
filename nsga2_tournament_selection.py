import random

def tournament_selection(population, fronts, distances, tournament_size=2):
    """
    Perform tournament selection on the population.
    
    Args:
    - population: list of Individual instances
    - fronts: list of lists, where each list contains the indices of solutions in that front
    - distances: list of crowding distances for each solution
    - tournament_size: number of individuals to be compared in the tournament
    
    Returns:
    - selected: list of selected Individual instances
    """
    selected = []
    
    while len(selected) < len(population):
        tournament = random.sample(range(len(population)), tournament_size)
        best = tournament[0]
        for competitor in tournament:
            if is_better(competitor, best, fronts, distances):
                best = competitor
        selected.append(population[best])
    
    return selected

def is_better(ind1, ind2, fronts, distances):
    """
    Determine if ind1 is better than ind2 based on rank and crowding distance.
    
    Args:
    - ind1: index of the first individual
    - ind2: index of the second individual
    - fronts: list of lists, where each list contains the indices of solutions in that front
    - distances: list of crowding distances for each solution
    
    Returns:
    - True if ind1 is better than ind2, False otherwise
    """
    for fi in range(len(fronts)):
        front = fronts[fi]
        ind1_front_index = -1
        ind2_front_index = -1
        if ind1 in front:
            ind1_front_index = fi
        if ind2 in front:
            ind2_front_index = fi

    if ind1_front_index < ind2_front_index:
        return True
    elif ind1_front_index == ind2_front_index:
        if distances[ind1] > distances[ind2]:
            return True
    return False
