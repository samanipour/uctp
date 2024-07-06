import numpy as np
import random
from sa import SimulatedAnnealing
from sa_maxtime  import MaxTimeTermination
from sa_unary import Unary
from sa_nullary import Nullary
from sa_gpm import GPM
from individual import Individual
from sa_tempschedular import LnTempSchedular
from sa_tempschedular import PolyTempSchedular
from sa_objective import UTCObjective
import inputs
from plot_results import plot_results


def evaluate():
    # Create a 2D Matrix for robot playground

    max_sem_num   =4
    cnum=10
    
    student_list = inputs.get_students()
    instructor_list = inputs.get_instructors()
    course_list = inputs.get_uni_programs()[0].courses #TODO: should consider all program courses
    uni_programs =inputs.get_uni_programs()

    nullary = Nullary(cnum,max_sem_num)
    unary = Unary()
    objective = UTCObjective(instructor_list=instructor_list,course_list=course_list,student_list=student_list,
                         uni_programs=uni_programs,min_load=12,max_load=24)
    gpm = GPM(max_sem_num)
    max_termination_time = 1 #In seconds

    # founded_solution_by_HC = []
    founded_solution_by_SA = []

    # for i in range(1,max_termination_time):
    #     termination = MaxTimeTermination(i)
    #     HC  = HillClimbing(random,gpm,nullary,unary,termination)
    #     best_found_solution = HC.solve(objective)
    #     founded_solution_by_HC.append((i,best_found_solution.y))
    fitness_scores = list()
    # for i in range(1,10):
    #     termination = MaxTimeTermination(max_termination_time)
    #     temp_schedular = PolyTempSchedular(t_start=10,epsilon=0.05)
    #     SA  = SimulatedAnnealing(random,temp_schedular,gpm=gpm,nullary=nullary,unary=unary,termination=termination)
    #     best_found_solution = SA.solve(objective)
    #     founded_solution_by_SA.append((i,best_found_solution.y))
    #     fitness_scores.append(best_found_solution.y)
    # print(f"founded solutions by HC {founded_solution_by_HC}")

    termination = MaxTimeTermination(max_termination_time)
    temp_schedular = PolyTempSchedular(t_start=10,epsilon=0.05)
    SA  = SimulatedAnnealing(random,temp_schedular,gpm=gpm,nullary=nullary,unary=unary,termination=termination)
    best_found_solution = SA.solve(objective)
    print(best_found_solution)
    # # founded_solution_by_SA.append((i,best_found_solution.y))
    # fitness_scores.append(best_found_solution.y)
    
    
    # print(f"founded solutions by SA {founded_solution_by_SA}")
    plot_results(fitness_scores)

    # plot_time_series(founded_solution_by_SA,founded_solution_by_HC,"SA","HC")

evaluate()