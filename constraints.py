from course import get_course
def prerequisites_violation_penalty(plan,uni_program_list):
    penalty = 0
    for program in uni_program_list:
        course_list = program.courses
        for i in len(plan):
            semester = plan[i]
            for course_id in semester:
                prerequisites = get_course(course_list,course_id).prerequisites
                if(i==0):
                    if(len(prerequisites) !=0):
                        penalty +=1
                else:
                    for j in range(i-1,i):
                        for prereq in prerequisites:
                            if prereq not in semester[j]:
                                penalty +=1
    return penalty

def corequisites_violation_penalty(plan,uni_program_list):
    penalty = 0
    for program in uni_program_list:
        course_list = program.courses
        for semester in plan:
            for course_id in semester:
                plan_course = get_course(course_list,course_id)
                plan_course_corequisites = plan_course.corequisite  
                for coreq_id in plan_course_corequisites:
                    if coreq_id not in semester:
                        penalty +=1
    return penalty
            
def plan_total_load_violation(plan,uni_program_list):
    penalty = 0
    for program in uni_program_list:
        course_list = program.courses
        total_load = 0
        for semester in plan:
            for course_id in semester:
                course = get_course(course_list,course_id)
                if course !=None:#course exists in this program
                    total_load +=course.load
        if total_load>program.mandatory_load + program.elective_load:
            penalty +=1
    return penalty

def student_load_violation(plan,uni_program_list,student_list):
    penalty = 0
    for student in student_list:
        student_program = get_program(student.program_id,uni_program_list) 
        student_program_min_load = student_program.min_load
        student_program_max_load = student_program.max_load
        student_program_mandatory_load = student_program.mandatory_load
        student_program_elective_load = student_program.elective_load
        student_program_courses = student_program.courses

        for course in student_program_courses:
            all_semester_course_id = list()
            for semester in plan:
                all_semester_course_id = all_semester_course_id + semester
            if course.id not in all_semester_course_id:
                penalty +=1 # student course not exists in any of semesters of plan
            
            total_plan_load = 0
            for semester in plan:
                semester_load = 0
                for sem_course_id in semester:
                    if course.id in sem_course_id:
                        semester_load += course.load
                        total_load_violation+=course.load
                if not (student_program_min_load<=semester_load<=student_program_max_load):
                    penalty+=1
            if total_plan_load != (student_program_mandatory_load+student_program_elective_load):
                penalty+=1
    return penalty
def total_violation(plan,uni_program_list,student_list):
    violation = 0
    violation += prerequisites_violation_penalty(plan,uni_program_list)
    violation += corequisites_violation_penalty(plan,uni_program_list)
    violation += plan_total_load_violation(plan,uni_program_list)
    violation += student_load_violation(plan,uni_program_list,student_list)
    return violation
def is_plan_feasible(plan,uni_program_list,student_list):
    violation = total_violation(plan,uni_program_list,student_list)
    if violation != 0:
        return False
    else:
        return True

def get_program(id,uni_program_list):
    for program in uni_program_list:
        if id == program.id:
            return program