class Student:
    def __init__(self,sid,program_id):
        self.id = sid
        self.max_load = 24
        self.min_load = 12
        self.courses = list()
        self.elective_courses = list()
        self.program_id = program_id
    
    def __str__(self) -> str:
        return "sid"+str(self.sid)