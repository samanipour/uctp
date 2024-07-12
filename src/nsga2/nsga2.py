import math
import random
from ..model.individual import Individual
from nsga2_non_dominated_sort import non_dominated_sorting
from nsga2_crowding_dist import crowding_distance
from nsga2_tournament_selection import ParetoTournament
from ..termination.maxtime import MaxTimeTermination
from ..helper import inputs
from ..gpm.gpm import GPM
from ..operator.nullary import Nullary
from ..operator.unary import MPX
from ..operator.binary import UCX
from ..objective import objective as MultiObjective
from ..helper.plot_results import *
class NSGA2:
    def __init__(self,random,gpm,nullary,unary,binary,selection,termination,pop_size=4,cr=0.7):
        self.random = random
        self.gpm = gpm
        self.nullary = nullary
        self.unary = unary
        self.binary = binary
        self.selection = selection
        self.termination = termination
        self.pop_size = pop_size
        self.mate_size = pop_size
        self.cr = cr
        self.pop = list()
        self.pbest = Individual()
        self.pbest.y = (-math.inf,math.inf,math.inf,math.inf,math.inf)
    def solve(self,objective): 
          
        mate_pool = list()
        pcur = Individual()

        fitness_scores_f1 = list()
        fitness_scores_f2 = list()
        fitness_scores_f3 = list()
        fitness_scores_f4 = list()
        fitness_scores_f5 = list()

        for i in range(self.pop_size):
            sol = Individual()
            sol.g = self.nullary.create(self.random)
            self.pop.append(sol)

        #2 Evaluate Population
        for i in range(self.pop_size):
            pop[i].x = self.gpm.gpm(pop[i].g)

            f1 = objective.total_instructor_course_priorities(plan=pop[i].x)
            f2 = objective.total_instructor_load_error(plan=pop[i].x)
            f3 = objective.total_students_courses(plan=pop[i].x)
            f4 = objective.student_load_balance_error(plan=pop[i].x)
            f5 = objective.students_final_load(plan=pop[i].x)
            # print(f1,f2,f3,f4,f5)
            pop[i].y = (f1,f2,f3,f4,f5)

        while (not self.termination.shouldTerminate()):
            #3 Rank solutions based on Pareto dominance
            fronts,fronts_individual = non_dominated_sorting(pop)
            # print(fronts)
            # Step 4: Calculate crowding distances for each front
            distances = [0] * len(pop)
            for front in fronts:
                front_distances = crowding_distance(pop, front)
                for i in range(len(front)):
                    distances[front[i]] = front_distances[front[i]]

            # Step 5: Perform tournament selection
            mate_pool = self.selection.select(pop, fronts, distances)
  
            offsprings=[]
            for i in range(self.mate_size):
                pcur = Individual()
                if (self.random.random() < self.cr):
                    j = self.random.randint(0,self.mate_size-1)
                    pcur = self.binary.recombine(mate_pool[i],mate_pool[j],self.random)
                else:
                    pcur = self.unary.mutate(mate_pool[i],self.random)
                offsprings.append(pcur)

            for i in range(self.pop_size):
                offsprings[i].x = self.gpm.gpm(offsprings[i].g)
                f1 = objective.total_instructor_course_priorities(plan=offsprings[i].x)
                f2 = objective.total_instructor_load_error(plan=offsprings[i].x)
                f3 = objective.total_students_courses(plan=offsprings[i].x)
                f4 = objective.student_load_balance_error(plan=offsprings[i].x)
                f5 = objective.students_final_load(plan=offsprings[i].x)
                # print(f1,f2,f3,f4,f5)
                offsprings[i].y = (f1,f2,f3,f4,f5)

            pop = []+offsprings

            # for p in pop:
            #     print(p.x,p.y)
            fronts,fronts_individual = non_dominated_sorting(pop)

            # Select the next generation population
            next_population = []
            for front in fronts_individual:
                if len(next_population) + len(front) <= self.pop_size:
                    next_population.extend(front)
                else:
                    front_distances = crowding_distance(pop, front)
                    sorted_front = sorted(zip(front, front_distances), key=lambda x: x[1], reverse=True)
                    next_population.extend([ind for ind, _ in sorted_front[:self.pop_size - len(next_population)]])
                    break
                
            pop = []+next_population

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

        fitness_scores = []
        fitness_scores.append(fitness_scores_f1)
        fitness_scores.append(fitness_scores_f2)
        fitness_scores.append(fitness_scores_f3)
        fitness_scores.append(fitness_scores_f4)
        fitness_scores.append(fitness_scores_f5)
        
        return fronts_individual,fitness_scores
    
def main():
    fitness_scores = list()
    best_founded_solution = Individual()
    max_semesters = inputs.get_max_terms()
    course_numbers = inputs.get_courses_nums()
    gpm = GPM()
    nullary = Nullary(cnum=course_numbers,max_semester_num=max_semesters)
    unary = MPX(max_semester_numbers=max_semesters)
    binary= UCX()
    selection = ParetoTournament()
    termination = MaxTimeTermination(10)
    objective = MultiObjective
    pop_size = 4
    cr = 0.7
    genetic = NSGA2(random=random,gpm=gpm,nullary=nullary,unary=unary,binary=binary,selection=selection,termination=termination,pop_size=pop_size,cr=cr)
    fitness_scores,best_founded_solution = genetic.solve(objective=objective)
    print(best_founded_solution)
    plot_lines(fitness_scores,['f1','f2','f3','f4','f5'])

if __name__ == "__main__":
    main()