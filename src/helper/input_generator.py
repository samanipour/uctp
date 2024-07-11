import random
import time
import json
def generate_course_instructor_semesters(course_nums,instructor_nums,max_term,random):
    course_instructor_sems=list()
    for i in range(course_nums):
        instructor_assignee = list()
        for j in range(instructor_nums):
            random_sem = random.randint(0,max_term)
            instructor_assignee.append(random_sem)
        course_instructor_sems.append(instructor_assignee)
    return course_instructor_sems

def generate_input(course_nums,instructor_nums,student_nums,program_nums,max_term,random):
    #generate programs:
    output_file = 'inputs/inputs'+'.json'
    instructors = list()
    for i in range(instructor_nums):
        ins_id = i+1
        ins_sems_loads = list()
        for s in range(max_term):
            ins_sems_loads.append(random.randint(3,12))
        ins_courses = list()
        for c in range(course_nums):
            ins_courses.append(c)
        ins_prios = list()
        for p in range(course_nums):
            ins_prios.append(random.randint(0,10))
        ins_type = random.randint(1,2)
        instructor = {}
        instructor['id']=ins_id
        instructor['semester_load']=ins_sems_loads
        instructor['courses']=ins_courses
        instructor['priorities']=ins_prios
        instructor['type']=ins_type
        instructors.append(instructor)

    students=list()
    for i in range(student_nums):
        s_id = i+1
        s_program_id= random.randint(1,program_nums)
        s_compeleted_courses=list()
        s_cur_sem=1
        student = {}
        student["id"]=s_id
        student["program_id"]=s_program_id
        student["complete_courses"]=s_compeleted_courses
        student["current_semester"]=s_cur_sem
        students.append(student)
    
    programs = list()
    
    for i in range(1,program_nums+1):
        program = {}
        courses = list()
        program["id"] = i
        program["mandatory_load"] = random.randint(112,120)
        program["elective_load"] = random.randint(0,24)
        program["min_load"] = random.randint(6,12)
        program["max_load"] = random.randint(12,24)
        program["program_degree"] = i
        program["max_term"] = random.randint(2,8)
        for j in range(course_nums):
            course = {}
            course["id"] = j
            course["name"] = "CS"+str(j)
            course["load_value"] = random.randint(0,6)
            course["prerequisites"] = list()
            course["corequisites"] = list()
            course["is_elective"] = random.choice([True, False])
            course["is_common"] = random.choice([True, False])
            courses.append(course)
        program["courses"] = courses
        programs.append(program)
        

    with open(output_file, 'w') as f:
        json.dump({"instructors": instructors,"students":students,"programs":programs}, f, indent=4)

generate_input(course_nums=10,instructor_nums=1,student_nums=1,program_nums=3,max_term=8,random=random)