class Unary:
    def __init__(self,max_sem_num) -> None:
        self.max_terms = max_sem_num

    def mutate(self,p,random):
        random__instructor_index = random.randint(0,len(p)-1)
        random_course_index = random.randint(0,len(p[0])-1)
        g = list()
        for i in range(len(p)):
            g.append(p[i])

        g[random__instructor_index][random_course_index] = random.randint(1,self.max_terms)
        while(random.random()<0.5):
            random__instructor_index = random.randint(0,len(p)-1)
            random_course_index = random.randint(0,len(p[0])-1)
            g[random__instructor_index][random_course_index] = random.randint(1,self.max_terms)

        return g