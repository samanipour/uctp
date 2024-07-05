from course import get_course
from inputs import get_program
def compute(plan,instructor_list,course_list,random):
    # for semester in semester_plan:

    # return total_instructor_load_error(plan,instructor_list,course_list)
    # return best_priorities_first(plan,instructor_list)
    return total_plan_load(plan,course_list)

def total_instructor_load_error(plan,instructor_list,uni_program_list):
    total_error = 0
    already_considered_ins_course = list()
    for i in range(len(instructor_list)):
        already_considered_ins_course.append(set())
    for program in uni_program_list:
        course_list = program.courses
        for instructor in instructor_list:
            instructor_course_ids = instructor.course_list
            instructor_total_load_error = 0
            instructor_load_list = instructor.load
            # sum_of_assigned_course_load = 0
            sum_of_assigned_course_sem_load = 0
            sem_load_error = 0
            for i in range(len(plan)-1):
                semester = plan[i]
                instructor_semester_load = instructor_load_list[i]
                for course_id in semester:
                    for ins_course_id in instructor_course_ids:
                        if course_id == ins_course_id:
                            course_load = get_course(course_list,course_id).load
                            course_program = get_program(course_id)
                            if course_id not in already_considered_ins_course[instructor.id]: # if its common course, then already exists in this list
                                already_considered_ins_course[instructor.id].add(course_id)
                                if course_program.program_degree != 1:#means it's Master or PhD program
                                    sum_of_assigned_course_sem_load+= (1.5 * course_load)
                                else:
                                    sum_of_assigned_course_sem_load+= course_load
                if instructor.type == 1:
                    sem_load_error = abs(instructor_semester_load-sum_of_assigned_course_sem_load)
                else:
                    sem_load_error = sum_of_assigned_course_sem_load
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

def total_students_load(plan,course_list,student_list,min_load,max_load):
    total_fitness = 0
    for student in student_list:
        student_load = [0]*len(plan) # number of semesters
        student_load_fitness = 0
        for i in range(plan):
            semester = plan[i]
            for course_id in semester:
                course_load = get_course(course_list,course_id).load
                student_load[i] += course_load
        
        # calculate to see if all semester loads are the same
        total_load = sum(student_load)
        avg_load = total_load/len(student_load)
        for sem_load in student_load:
            if (abs(sem_load-avg_load)>=1):
                student_load_fitness +=1
            if(min_load <= sem_load <= max_load):
                student_load_fitness +=1

        sorted_loads = sorted(student_load)
        if (student_load[len(student_load)-1] == sorted_loads[0]):
            student_load_fitness+=1

        total_fitness+=student_load_fitness
    return total_load

def total_students_courses(plan,course_list,student_list):
    number_of_courses = 0
    for semester in plan:
        number_of_courses += len(semester)

    student_number_of_course = [0]*number_of_courses
    for semester in plan:
        for course_id in semester:
            for student in student_list:
                if course_id in student.courses or course_id in student.elective_courses:
                    student_number_of_course[course_id]+=1

    total_register_students = sum(student_number_of_course)
    course_student_fitness = total_register_students / number_of_courses

    #TODO: calculate total faculty course load //lower better

    return course_student_fitness

