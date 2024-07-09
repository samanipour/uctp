from individual import Individual
import copy
def mutate(p,max_terms,random):
    random_instructor_index = random.randint(0,len(p.g)-1)
    random_course_index = random.randint(0,len(p.g[0])-1)
    ofs = Individual()
    ofs.g = copy.deepcopy(p.g)
    ofs.g[random_instructor_index][random_course_index] = random.randint(1,max_terms)
    while(random.random()<0.8):
        random__instructor_index = random.randint(0,len(p.g)-1)
        random_course_index = random.randint(0,len(p.g[0])-1)
        ofs.g[random__instructor_index][random_course_index] = random.randint(1,max_terms)
    return ofs
    