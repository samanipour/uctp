class Course:
    def __init__(self,input_id):
        self.id = input_id
        self.load = 2
        self.name = "course_name"
        self.prerequisites = list()
        self.corequisite = list()
        self.is_elective = False
    def __str__(self) -> str:
        return "cid"+str(self.id)

def get_course_load(course_list,course_id):
    for course in course_list:
        if course.id == course_id:
            return course.load