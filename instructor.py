class Instructor:
    def __init__(self,id,course_list_id,instructor_load_list,priorities,ins_type):
        self.id = id
        self.course_list = course_list_id
        self.type = ins_type
        self.load = instructor_load_list
        self.priorities = priorities

    def __str__(self):
        return "Courses"+str(self.course_list)+'\n'+"load list"+str(self.load)