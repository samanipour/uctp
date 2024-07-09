import inputs
def compute(plan):
        ie = total_instructor_load_error(plan)
        bpf= total_instructor_course_priorities(plan)
        tls= total_students_courses(plan)
        slb =student_load_balance_error(plan)
        sfl =students_final_load(plan)
        fitness = ie + bpf + (1/1+tls)+slb+sfl #TODO: should add weights 
        return fitness

def total_instructor_load_error(plan):
    total_error = 0
    already_considered_ins_course = list()
    for i in range(len(inputs.get_instructors())):
        already_considered_ins_course.append(set())

    for i in range(len(plan)):
        instructor_course_sems = plan[i]
        instructor = inputs.get_instructor(i+1)
        
        instructor_course_ids = instructor.course_list
        instructor_total_load_error = 0
        sum_of_assigned_course_sem_load = 0
        for j in range(len(instructor_course_sems)):
            instructor_course_sem_id = instructor_course_sems[j]# sem_id of instructor_id=i and course_id=j 
            if j in instructor_course_ids and instructor_course_sem_id != 0: #zero sem_id means that the instructor dos not present that course
                course_load = inputs.get_course(j).load
                course_program = inputs.get_course_program(j)
                if j not in already_considered_ins_course[instructor.id-1]: # if its common course, then already exists in this list
                    already_considered_ins_course[instructor.id-1].add(j)
                    if course_program.program_degree != 1:#means it's Master or PhD program
                        sum_of_assigned_course_sem_load+= (1.5 * course_load)
                    else:
                        sum_of_assigned_course_sem_load+= course_load
        if instructor.type == 1:
            instructor_total_load_error = abs(sum(instructor.load)-sum_of_assigned_course_sem_load)
        else:
            instructor_total_load_error = sum_of_assigned_course_sem_load
        total_error +=instructor_total_load_error
    return total_error
def total_instructor_course_priorities(plan):
    total_prio_fitness = 0
    for i in range(len(plan)):
        instructor_course_sems = plan[i]
        instructor = inputs.get_instructor(i+1)
        instructor_course_ids = instructor.course_list
        instructor_priorities = instructor.priorities
        instructor_prio_fitness = 0
        for j in range(len(instructor_course_sems)):
            instructor_course_sem_id = instructor_course_sems[j]# sem_id of instructor_id=i and course_id=j 
            if j in instructor_course_ids and instructor_course_sem_id != 0:
                ins_course_priority = instructor_priorities[j]
                instructor_prio_fitness += (1/(1+ins_course_priority)) #we want to maximize
        total_prio_fitness += instructor_prio_fitness
    return total_prio_fitness
def total_students_courses(plan):
    number_of_courses = len(plan[0])
    student_list = inputs.get_students()
    student_number_of_course = [0]*number_of_courses
    for i in range(len(plan)):
        instructor_course_sems = plan[i]
        for j in range(len(instructor_course_sems)):
            instructor_course_sem_id = instructor_course_sems[j]# sem_id of instructor_id=i and course_id=j 
            for student in student_list:
                student_course_ids = [c.id for c in student.courses] + [c.id for c in student.elective_courses]
                if j in student_course_ids:
                    student_number_of_course[j]+=1
    total_register_students = sum(student_number_of_course)
    course_student_fitness = total_register_students / number_of_courses

    #TODO: calculate total faculty course load //lower better

    return course_student_fitness 
def student_load_balance_error(plan):
    total_fitness = 0
    student_list = inputs.get_students()
    for student in student_list:
        student_load = [0]*len(plan) # number of semesters
        student_load_fitness = 0

        student_courses = student.courses + student.elective_courses
        student_courses_ids = [c.id for c in student_courses]
        student_program_id = student.program_id
        student_program = inputs.get_program(student_program_id)
        ideal_load = (student_program.mandatory_load + student_program.optional_load)/len(student_program.courses)
        for i in range(len(plan)):
            instructor_course_sems = plan[i]
            for j in range(len(instructor_course_sems)):
                instructor_course_sem_id = instructor_course_sems[j]# sem_id of instructor_id=i and course_id=j
                if j in student_courses_ids:
                    course_load = inputs.get_course(j).load
                    student_load[i] += course_load

        for sem_load in student_load:
            student_load_fitness += abs(sem_load-ideal_load)
        total_fitness+=student_load_fitness
    return total_fitness 
def students_final_load(plan):
    total_fitness = 0
    student_list = inputs.get_students()
    for student in student_list:
        final_sem_load = 0
        student_courses = student.courses + student.elective_courses
        student_courses_ids = [c.id for c in student_courses]
        student_program_id = student.program_id
        student_program = inputs.get_program(student_program_id)
        student_max_term = student_program.max_term
        for i in range(len(plan)):
            instructor_course_sems = plan[i]
            for j in range(len(instructor_course_sems)):
                instructor_course_sem_id = instructor_course_sems[j]# sem_id of instructor_id=i and course_id=j
                if j in student_courses_ids and instructor_course_sem_id == student_max_term:
                    course_load = inputs.get_course(j).load
                    final_sem_load += course_load
        total_fitness +=final_sem_load
    return total_fitness