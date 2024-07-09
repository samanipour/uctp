import math
import numpy as np
from course import get_course
from inputs import get_course_program
import objective2
class UTCObjective:
    # def __init__(self,instructor_list,course_list,student_list,uni_programs,min_load,max_load):
    #     self.instructor_list=instructor_list
    #     self.course_list=course_list
    #     self.student_list=student_list
    #     self.uni_programs=uni_programs
    #     self.min_load=min_load
    #     self.max_load=max_load
    def compute(self,plan):
        ie = objective2.total_instructor_load_error(plan)
        bpf= objective2.total_instructor_course_priorities(plan)
        tls= objective2.total_students_courses(plan)
        slb = objective2.student_load_balance_error(plan)
        sfl = objective2.students_final_load(plan)
        fitness = ie + bpf + (1/1+tls)+slb+sfl #TODO: should add weights 
        return fitness

    
def main():
    pass
if __name__=="__main__":
    main()
