from ..model.individual import Individual
import copy
class MPX:
    def __init__(self,max_semester_numbers):
        self.max_semester_numbers = max_semester_numbers
        
    def mutate(self,parent,random):
        random_instructor_index = random.randint(0,len(parent.g)-1)
        random_course_index = random.randint(0,len(parent.g[0])-1)
        ofs = Individual()
        ofs.g = copy.deepcopy(parent.g)
        ofs.g[random_instructor_index][random_course_index] = random.randint(1,self.max_semester_numbers)
        while(random.random()<0.8):
            random__instructor_index = random.randint(0,len(parent.g)-1)
            random_course_index = random.randint(0,len(parent.g[0])-1)
            ofs.g[random__instructor_index][random_course_index] = random.randint(1,self.max_semester_numbers)
        return ofs
    