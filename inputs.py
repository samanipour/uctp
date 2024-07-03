import json
from instructor import Instructor
from course import Course
from student import Student

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
        course = Course(id)
        course.name = name
        course.load = load_value
        course.prerequisites = prerequisites
        course.corequisite = corequisites
        course.is_elective = is_elective
        course_list.append(course)
    return course_list
def get_uni_plans():
    for plan in data['plans']:
        plan_id = plan['id']
        plan_mandatory_load = plan['mandatory_load']
        plan_optional_load = plan['optional_load']
        plan_courses = get_courses(plan)
        
def get_students():
    student_list = list()
    for student in data['students']:
        id = student['id']
        courses = student['courses']
        elective_courses=student["elective_courses"]
        min_load = student["min_load"]
        max_load = student["max_load"]
        student = Student(id)
        student.courses = courses
        student.elective_courses = elective_courses
        student.max_load = min_load
        max_load = max_load
        student_list.append(student)
    return student_list

if __name__ == "__main__":
    for ins in get_instructors():
        print(ins.course_list)
    #
    # for c in get_courses():
    #     print(c.is_elective)
    # for s in get_students():
    #     print(s.id)