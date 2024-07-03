# import random
import math
from course import get_course_load
def compute(plan,instructor_list,course_list,random):
    # for semester in semester_plan:

    # return total_instructor_load_error(plan,instructor_list,course_list)
    # return best_priorities_first(plan,instructor_list)
    return total_plan_load(plan,course_list)

def total_instructor_load_error(plan,instructor_list,course_list):
    total_error = 0
    for instructor in instructor_list:
        instructor_course_ids = instructor.course_list
        instructor_total_load_error = 0
        instructor_load_list = instructor.load
        # sum_of_assigned_course_load = 0
        sum_of_assigned_course_sem_load = 0
        sem_load_error = 0
        for i in range(len(plan)-1):
            semester = plan[i]
            instructor_semseter_load = instructor_load_list[i]
            for course_id in semester:
                for ins_course_id in instructor_course_ids:
                    if course_id == ins_course_id:
                        sum_of_assigned_course_sem_load+=get_course_load(course_list,course_id)
            
            sem_load_error = (instructor_semseter_load-sum_of_assigned_course_sem_load)**2
            instructor_total_load_error +=sem_load_error
        total_error+=instructor_total_load_error
    return total_error

def best_priorities_first(plan,instructor_list):
    total_prio_fitness = 0
    for semester in plan:
        instructor_prio_fintness = 0
        for course_id in semester:
            for instructor in instructor_list:
                ins_priorities = instructor.priorities
                ins_courses = instructor.course_list
                for ins_c in ins_courses:
                    if (course_id == ins_c):
                        index = ins_courses.index(course_id)
                        ins_course_priority = ins_priorities[index]
                        instructor_prio_fintness += ins_course_priority #lower fitness is better
                        # print(f"cid{course_id} cp{ins_course_priority} tot{instructor_prio_fintness}")
                        # print(instructor_prio_fintness)
            # print(f">>>>>>>>tot{instructor_prio_fintness}")
        total_prio_fitness += instructor_prio_fintness
    return total_prio_fitness    

def total_plan_load(plan,course_list):
    total_load = 0
    for semester in plan:
        for course_id in semester:
            for course in course_list:
                if course_id == course.id:
                    total_load += course.load
    return total_load
        


