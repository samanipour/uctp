# import datetime
import time
import json
from inputs import get_instructors
from inputs import get_students

def save_plan(plan,instructor_list,student_list):
    output_file = 'outputs/plan'+str(time.time())+'.json'
    output_plan = {}
    for i in range (len(plan)):
        semester = plan[i]
        output_semester = {}
        for j in range(len(semester)):
            course_id = semester[j]
            output_course = {}
            output_instructors=[]
            output_students=[]

            for k in range(len(instructor_list)):
                instructor = instructor_list[k]
                if course_id in instructor.course_list:
                    output_instructors.append(instructor.id)
            
            for k in range(len(student_list)):
                student = student_list[k]
                if course_id in student.courses or course_id in student.elective_courses:
                    output_students.append(student.id)

            output_course['Instructors']=output_instructors
            output_course['Students']=output_students
            output_semester['Course Id'+str(j)]=output_course
        output_plan['Semester '+str(i+1)] = output_semester
        
    with open(output_file, 'w') as f:
        json.dump({"Plan": output_plan}, f, indent=4)

if __name__ == '__main__':
    plan =[
        [1,2,3],
        [4,5,6]
    ]
    instructors = get_instructors()
    students = get_students()
    save_plan(plan,instructors,students)