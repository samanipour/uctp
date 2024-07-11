import random
import math
from model.individual import Individual
from gpm.gpm import gpm
# from objective import compute
import objective.objective as objective
from course import Course
from student import Student
from instructor import Instructor

from genetic.tournament import select
from ux import recombine
from genetic.multimutate import mutate
import helper.inputs as inputs
from helper.plot_results import plot_lines
import nsga.nsga2_non_dominated_sort as nsga2_non_dominated_sort
from nsga.nsga2_crowding_dist import crowding_distance
from nsga.nsga2_tournament_selection import tournament_selection
#TODO: these parameters should obtains from input data
cnum = 10
max_semester_num = 4
ins_min_load = 3
ins_max_load = 24

# genetic algo
pop_size = 4

sol = Individual()
sol.g = [-1] * cnum #chromosome size
pop = list()

for i in range(pop_size):
    sol = Individual()
    sol.g = [-1] * cnum #chromosome size
    for i in range(cnum):
        random_sem = random.randint(1,max_semester_num)
        sol.g[i] = random_sem
    pop.append(sol)

t=0
pbest = Individual()
pcur = Individual()

pbest.y = (-math.inf,math.inf,math.inf,math.inf,math.inf)
mate_pool = list()
mate_size = pop_size
cr = 0.7
student_list = inputs.get_students()
instructor_list = inputs.get_instructors()
course_list = inputs.get_uni_programs()[0].courses #TODO: should consider all program courses
uni_programs =inputs.get_uni_programs()
fitness_scores_f1 = list()
fitness_scores_f2 = list()
fitness_scores_f3 = list()
fitness_scores_f4 = list()
fitness_scores_f5 = list()

#2 Evaluate Population
for i in range(pop_size):
    pop[i].x = gpm(pop[i].g,max_semester_num)

    f1 = objective.total_instructor_course_priorities(plan=pop[i].x,instructor_list=instructor_list)
    f2 = objective.total_instructor_load_error(plan=pop[i].x,instructor_list=instructor_list,uni_program_list=uni_programs)
    f3 = objective.total_students_courses(plan=pop[i].x,course_list=course_list,student_list=student_list)
    f4 = objective.student_load_balance_error(plan=pop[i].x,course_list=course_list,student_list=student_list)
    f5 = objective.students_final_load(plan=pop[i].x,course_list=course_list,student_list=student_list)
    # print(f1,f2,f3,f4,f5)
    pop[i].y = (f1,f2,f3,f4,f5)

while (t < 100):
    #3 Rank solutions based on Pareto dominance
    fronts,fronts_individual = nsga2_non_dominated_sort.non_dominated_sorting(pop)
    # print(fronts)
    # Step 4: Calculate crowding distances for each front
    distances = [0] * len(pop)
    for front in fronts:
        front_distances = crowding_distance(pop, front)
        for i in range(len(front)):
            distances[front[i]] = front_distances[front[i]]

    # Step 5: Perform tournament selection
    mate_pool = tournament_selection(pop, fronts, distances)

    offsprings=[]
    for i in range(mate_size):
        pcur = Individual()
        if (random.random() < cr):
            j = random.randint(0,mate_size-1)
            pcur = recombine(mate_pool[i],mate_pool[j],random)
        else:
            pcur = mutate(mate_pool[i],max_semester_num,random)
        offsprings.append(pcur)
    
    for i in range(pop_size):
        offsprings[i].x = gpm(offsprings[i].g,max_semester_num)
        f1 = objective.total_instructor_course_priorities(plan=offsprings[i].x,instructor_list=instructor_list)
        f2 = objective.total_instructor_load_error(plan=offsprings[i].x,instructor_list=instructor_list,uni_program_list=uni_programs)
        f3 = objective.total_students_courses(plan=offsprings[i].x,course_list=course_list,student_list=student_list)
        f4 = objective.student_load_balance_error(plan=offsprings[i].x,course_list=course_list,student_list=student_list)
        f5 = objective.students_final_load(plan=offsprings[i].x,course_list=course_list,student_list=student_list)
        # print(f1,f2,f3,f4,f5)
        offsprings[i].y = (f1,f2,f3,f4,f5)

    pop = []+offsprings
    
    # for p in pop:
    #     print(p.x,p.y)
    fronts,fronts_individual = nsga2_non_dominated_sort.non_dominated_sorting(pop)

    # Select the next generation population
    next_population = []
    for front in fronts_individual:
        if len(next_population) + len(front) <= pop_size:
            next_population.extend(front)
        else:
            front_distances = crowding_distance(pop, front)
            sorted_front = sorted(zip(front, front_distances), key=lambda x: x[1], reverse=True)
            next_population.extend([ind for ind, _ in sorted_front[:pop_size - len(next_population)]])
            break
    
    pop = []+next_population
    # print(f"iteration{t}>>>>>>>>>>>>>>>>>")
    # for fi in range(len(fronts_individual)):
    #     f = fronts_individual[fi]
    #     print(f"front {fi} ==============================")
    #     for ind in f:
    #         print(ind.y)

    best_fitness_f1 = min(ind.y[0] for ind in pop)  # Assuming y[0] corresponds to the primary objective
    fitness_scores_f1.append(best_fitness_f1)
    best_fitness_f2 = min(ind.y[1] for ind in pop)  # Assuming y[0] corresponds to the primary objective
    fitness_scores_f2.append(best_fitness_f2)
    best_fitness_f3 = min(ind.y[2] for ind in pop)  # Assuming y[0] corresponds to the primary objective
    fitness_scores_f3.append(best_fitness_f3)
    best_fitness_f4 = min(ind.y[3] for ind in pop)  # Assuming y[0] corresponds to the primary objective
    fitness_scores_f4.append(best_fitness_f4)
    best_fitness_f5 = min(ind.y[4] for ind in pop)  # Assuming y[0] corresponds to the primary objective
    fitness_scores_f5.append(best_fitness_f5)

    t+=1
fitness_scores = []

fitness_scores.append(fitness_scores_f1)
fitness_scores.append(fitness_scores_f2)
fitness_scores.append(fitness_scores_f3)
fitness_scores.append(fitness_scores_f4)
fitness_scores.append(fitness_scores_f5)

plot_lines(fitness_scores,['f1','f2','f3','f4','f5'])