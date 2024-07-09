import math
import numpy as np
import inputs
class Nullary:
    def __init__(self,cnum,max_semester_num):
        self.cnum = cnum
        self.max_semester_num=max_semester_num
    def create(self,random):
        # sol = Individual()
        g = list()
        for i in range(len(inputs.get_instructors())):
            instructor_course_list = list()
            for j in range(self.cnum):
                random_sem = random.randint(0,self.max_semester_num)
                instructor_course_list.append(random_sem)
            g.append(instructor_course_list)
        return g

def main():
    pass

if __name__=="__main__":
    main()