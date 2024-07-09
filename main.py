import inputs
def solve_by_sa():
    nullary = Nullary(cnum,max_sem_num)
    unary = Unary()
    objective = UTCObjective(instructor_list=instructor_list,course_list=course_list,student_list=student_list,
                         uni_programs=uni_programs,min_load=12,max_load=24)
    gpm = GPM(max_sem_num)
    max_termination_time = 100 #In seconds
    termination = MaxTimeTermination(max_termination_time)
    temp_schedular = PolyTempSchedular(t_start=10,epsilon=0.05)
    SA  = SimulatedAnnealing(random,temp_schedular,gpm=gpm,nullary=nullary,unary=unary,termination=termination)
    best_found_solution = SA.solve(objective)

def solve_by_ge():
    pass
def solve_by_nsga2():
    pass

def main():
    max_sem_num = 8
    cnum = 30
    
    student_list = inputs.get_students()
    instructor_list = inputs.get_instructors()
    course_list = inputs.get_uni_programs()[0].courses #TODO: should consider all program courses
    uni_programs=inputs.get_uni_programs()