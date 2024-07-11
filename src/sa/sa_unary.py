class Unary:

    def mutate(self,random,p,max_terms):
        random_index = random.randint(0,len(p)-1)
        # ofs = Individual()
        g = []+p
        g[random_index] = random.randint(1,max_terms)
        while(random.random()<0.5):
            random_index = random.randint(0,len(p)-1)
            g[random_index] = random.randint(1,max_terms)

        return g
