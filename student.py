class Student:
    def __init__(self,sid):
        self.id = sid
        self.max_load = 24
        self.min_load = 12
        self.courses = list()
        self.elective_courses = list()
    
    def __str__(self) -> str:
        return "sid"+str(self.sid)