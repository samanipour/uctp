import src.nsga2.constraint_domination as constraint_domination
def non_dominated_sorting(population):
    """
    Perform non-dominated sorting on the population.
    
    Args:
    - population: list of Individual instances
    
    Returns:
    - fronts: list of lists, where each list contains the indices of solutions in that front
    """
    S = [[] for _ in range(len(population))]
    front = [[]]
    fronts_individuals=[[]]
    n = [0 for _ in range(len(population))]
    rank = [0 for _ in range(len(population))]
    
    for p in range(len(population)):
        S[p] = []
        n[p] = 0
        for q in range(len(population)):
            if constraint_domination.dominates(population[p].y, population[q].y):
                S[p].append(q)
            elif constraint_domination.dominates(population[q].y, population[p].y):
                n[p] += 1
        
        if n[p] == 0:
            rank[p] = 0
            front[0].append(p)
            fronts_individuals[0].append(population[p])
    
    i = 0
    while front[i]:
        Q = []
        Q_individuals = []
        for p in front[i]:
            for q in S[p]:
                n[q] -= 1
                if n[q] == 0:
                    rank[q] = i + 1
                    Q.append(q)
                    Q_individuals.append(population[q])
        i += 1
        front.append(Q)
        fronts_individuals.append(Q_individuals)
    
    front.pop()
    return front,fronts_individuals

def dominates(fitness1, fitness2):
    """
    Check if fitness1 dominates fitness2.
    
    Args:
    - fitness1: tuple of objective values
    - fitness2: tuple of objective values
    
    Returns:
    - True if fitness1 dominates fitness2, False otherwise
    """
    # print(f"fitness 1 {fitness1}")
    return all(x <= y for x, y in zip(fitness1, fitness2)) and any(x < y for x, y in zip(fitness1, fitness2))
