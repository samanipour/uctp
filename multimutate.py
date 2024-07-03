from individual import Individual
def mutate(p,max_terms,random):
    random_index = random.randint(0,len(p.g)-1)
    ofs = Individual()
    ofs.g = []+p.g
    ofs.g[random_index] = random.randint(1,max_terms)
    while(random.random()<0.5):
        random_index = random.randint(0,len(p.g)-1)
        ofs.g[random_index] = random.randint(1,max_terms)

    return ofs

    