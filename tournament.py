def select(pop,tournament_size,random):
    mate_pool = list()
    for i in range(len(pop)):
        random_index = random.randint(0,len(pop)-1)
        p1 = pop[random_index]
        for j in range(tournament_size-1):
            random_index2 = random.randint(0,len(pop)-1)
            p2 = pop[random_index2]
            if(p2.y < p1.y):
                p1 = p2
        mate_pool.append(p1)
    return mate_pool
