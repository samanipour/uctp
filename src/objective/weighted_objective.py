from .objective import *
class WeightedObjective:
    def compute(self,plan):
        ie = total_instructor_load_error(plan)
        bpf= total_instructor_course_priorities(plan)
        tls= total_students_courses(plan)
        slb =student_load_balance_error(plan)
        sfl =students_final_load(plan)
        fitness = ie + bpf + (1/1+tls)+slb+sfl #TODO: should add weights 
        return fitness
        