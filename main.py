import inputs
from sa_objective2 import UTCObjective
from sa_unary2 import Unary
from sa_nullary2 import Nullary
from sa_gpm2 import GPM
from sa_tempschedular import LnTempSchedular
from sa_tempschedular import PolyTempSchedular
from sa import SimulatedAnnealing
from sa_maxtime  import MaxTimeTermination
import random
import math
from individual import Individual
from gpm2 import gpm
from objective2 import compute
import objective2
from tournament import select
from ux2 import recombine
from multimutate2 import mutate
import inputs
from plot_results import plot_results
import random
from plot_results import plot_lines
import nsga2_non_dominated_sort2
from nsga2_crowding_dist import crowding_distance
from nsga2_tournament_selection import tournament_selection
def solve_by_sa(cnum,max_sem_num,random):
    nullary = Nullary(cnum,max_sem_num)
    unary = Unary(max_sem_num)
    objective = UTCObjective()
    gpm = GPM()
    max_termination_time = 20 #In seconds
    termination = MaxTimeTermination(max_termination_time)
    temp_schedular = PolyTempSchedular(t_start=10,epsilon=0.05)
    SA  = SimulatedAnnealing(random,temp_schedular,gpm=gpm,nullary=nullary,unary=unary,termination=termination)
    best_found_solution = SA.solve(objective)
    return best_found_solution

def solve_by_ge(cnum,max_sem_num,random):
    

    # genetic algo
    pop_size = 4    
    pop = list()

    for i in range(pop_size):
        sol = Individual()
        g = list()
        for i in range(len(inputs.get_instructors())):
            instructor_course_list = list()
            for j in range(cnum):
                random_sem = random.randint(0,max_sem_num)
                instructor_course_list.append(random_sem)
            g.append(instructor_course_list)    
        sol.g = g
        pop.append(sol)

    t=0
    pbest = Individual()
    pcur = Individual()
    pbest.y = math.inf
    mate_pool = list()
    mate_size = pop_size
    cr = 0.7
    fitness_scores = list()
    while (t < 10):
        for i in range(pop_size):
            pcur = pop[i]
            pcur.x = gpm(pcur.g)
            pcur.y = compute(pcur.x)

            if (pcur.y<pbest.y):
                pbest = pcur

        mate_pool = select(pop,3,random)
        for i in range(mate_size):
            pcur = Individual()
            if (random.random() < cr):
                j = random.randint(0,mate_size-1)
                pcur = recombine(mate_pool[i],mate_pool[j],random)
            else:
                pcur = mutate(p=mate_pool[i],max_terms=max_sem_num,random=random)
            pop[i] = pcur
        print(f"iteration{t}")
        t+=1
        fitness_scores.append(pbest.y)
    plot_results(fitness_scores)



def solve_by_nsga2(cnum,max_sem_num,random):
    # genetic algo
    pop_size = 4    
    pop = list()

    for i in range(pop_size):
        sol = Individual()
        g = list()
        for i in range(len(inputs.get_instructors())):
            instructor_course_list = list()
            for j in range(cnum):
                random_sem = random.randint(0,max_sem_num)
                instructor_course_list.append(random_sem)
            g.append(instructor_course_list)    
        sol.g = g
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
        pop[i].x = gpm(pop[i].g)

        f1 = objective2.total_instructor_course_priorities(plan=pop[i].x)
        f2 = objective2.total_instructor_load_error(plan=pop[i].x)
        f3 = objective2.total_students_courses(plan=pop[i].x)
        f4 = objective2.student_load_balance_error(plan=pop[i].x)
        f5 = objective2.students_final_load(plan=pop[i].x)
        # print(f1,f2,f3,f4,f5)
        pop[i].y = (f1,f2,f3,f4,f5)

    while (t < 10):
        #3 Rank solutions based on Pareto dominance
        fronts,fronts_individual = nsga2_non_dominated_sort2.non_dominated_sorting(pop)
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
                pcur = mutate(mate_pool[i],max_sem_num,random)
            offsprings.append(pcur)

        for i in range(pop_size):
            offsprings[i].x = gpm(offsprings[i].g)
            f1 = objective2.total_instructor_course_priorities(plan=offsprings[i].x)
            f2 = objective2.total_instructor_load_error(plan=offsprings[i].x)
            f3 = objective2.total_students_courses(plan=offsprings[i].x)
            f4 = objective2.student_load_balance_error(plan=offsprings[i].x)
            f5 = objective2.students_final_load(plan=offsprings[i].x)
            # print(f1,f2,f3,f4,f5)
            offsprings[i].y = (f1,f2,f3,f4,f5)

        pop = []+offsprings

        # for p in pop:
        #     print(p.x,p.y)
        fronts,fronts_individual = nsga2_non_dominated_sort2.non_dominated_sorting(pop)

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


def main():
    max_sem_num = inputs.get_max_terms()
    cnum = inputs.get_courses_nums()
    solve_by_sa(max_sem_num=max_sem_num,cnum=cnum,random=random)
    solve_by_ge(cnum=cnum,max_sem_num=max_sem_num,random=random)
    # solve_by_nsga2(cnum=cnum,max_sem_num=max_sem_num,random=random)

main()