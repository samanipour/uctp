class UniProgram:
    def __init__(self,id,min_load,max_load,mandatory_load,optional_load,courses,program_degree,program_max_term):
        self.id = id
        self.mandatory_load = mandatory_load
        self.optional_load = optional_load
        self.min_load = min_load
        self.max_load = max_load
        self.courses = courses
        self.program_degree = program_degree
        self.max_term = program_max_term