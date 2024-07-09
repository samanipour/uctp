import json
from instructor import Instructor
from course import Course
from student import Student
from uni_program import UniProgram
# Load the JSON data
with open('inputs.json', 'r') as f:
    data = json.load(f)

def get_instructor_semesters_load(instructor_id):
    for instructor in data['instructors']:
        if instructor['id'] == instructor_id:
            return instructor['semester_load']
    return None  # Return None if no instructor with the given ID is found

def get_instructor_courses(instructor_id):
    for instructor in data['instructors']:
        if instructor['id'] == instructor_id:
            return instructor['courses']
    return None  # Return None if no instructor with the given ID is found
def get_instructors():
    instructor_list = list()
    # for i in range(1,len(data['instructors'])+1):
    #     ins_load_list = get_instructor_semesters_load(i)
    #     ins_course_list = get_instructor_courses(i)
    #     instructor = Instructor(ins_course_list,ins_load_list)
    #     instructor_list.append(instructor)
    for ins in data['instructors']:
        ins_id = ins['id']
        ins_priorities = ins['priorities']
        ins_type = ins['type']
        ins_load_list = ins['semester_load']
        ins_course_list = ins['courses']
        instructor = Instructor(ins_id,ins_course_list,ins_load_list,ins_priorities,ins_type)
        instructor_list.append(instructor)


    return instructor_list
        # print(instructor)
def get_courses(data):
    course_list = list()
    for course in data['courses']:
        # print(course)
        id=course['id']
        name=course['name']
        load_value=course['load_value']
        prerequisites=course['prerequisites']
        corequisites=course['corequisites'] 
        is_elective=course['is_elective']
        program_id =data['id']
        course = Course(id)
        course.name = name
        course.load = load_value
        course.prerequisites = prerequisites
        course.corequisite = corequisites
        course.is_elective = is_elective
        course.program_id = program_id
        course_list.append(course)
    return course_list
def get_uni_programs():
    programs = list()
    for program in data['programs']:
        program_id = program['id']
        program_min_load = program['min_load']
        program_max_load = program['max_load']
        program_mandatory_load = program['mandatory_load']
        program_optional_load = program['elective_load']
        program_degree = program['program_degree']
        program_max_term = program['max_term']
        program_courses = get_courses(program)
        program = UniProgram(id=program_id,min_load=program_min_load,max_load=program_max_load,mandatory_load=program_mandatory_load,
                             optional_load=program_optional_load,courses=program_courses,program_degree=program_degree,program_max_term=program_max_term)
        programs.append(program)
    return programs
        
def get_students():
    student_list = list()
    for student in data['students']:
        id = student['id']
        program_id=student['program_id']
        student_program = get_program(program_id)
        courses = student_program.courses
        elective_courses=[courses[i] for i in range(len(courses)) if courses[i].is_elective == True]
        min_load = student_program.min_load
        max_load = student_program.max_load
        student = Student(id,program_id)
        student.courses = courses
        student.elective_courses = elective_courses
        student.min_load = min_load
        student.max_load = max_load
        student_list.append(student)
    return student_list
def get_course(course_id):
    programs = get_uni_programs()
    for p in programs:
        program_courses = p.courses
        for course in program_courses:
            if course.id == course_id:
                return course
def get_program(id):
    for program in get_uni_programs():
        if program.id == id:
            return program
def get_course_program(course_id):
    for program in get_uni_programs():
        for course in program.courses:
            if course_id == course.id:
                return program
def get_instructor(ins_id):
    instructors = get_instructors()
    for ins in instructors:
        if (ins_id == ins.id):
            return ins
        
def get_courses_nums():
    return 30
def get_max_terms():
    return 8
if __name__ == "__main__":
    for ins in get_instructors():
        print(ins.course_list)
