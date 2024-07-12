from ..model.individual import Individual
from ..helper import inputs
import math
from ..gpm.gpm import GPM
from ..operator.nullary import Nullary
from ..operator.unary import MPX
from ..operator.binary import UCX
from .tournament import Tournament
from ..termination.maxtime import MaxTimeTermination
import random
from ..helper.plot_results import *
from ..objective.weighted_objective import WeightedObjective
class GE:
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
        self.pbest.y = math.inf
    def solve(self,objective):
        fitness_scores = list()
        pcur = Individual()
        mate_pool = list()

        for i in range(self.pop_size):
            sol = Individual()
            sol.g = self.nullary.create(self.random)
            self.pop.append(sol)

        while (not self.termination.shouldTerminate()):
            for i in range(self.pop_size):
                pcur = self.pop[i]
                pcur.x = self.gpm.gpm(pcur.g)
                pcur.y = objective.compute(pcur.x)

                if (pcur.y<self.pbest.y):
                    self.pbest = pcur

            mate_pool = self.selection.select(self.pop,3,self.random)
            for i in range(self.mate_size):
                pcur = Individual()
                if (self.random.random() < self.cr):
                    j = self.random.randint(0,self.mate_size-1)
                    pcur = self.binary.recombine(mate_pool[i],mate_pool[j],self.random)
                else:
                    pcur = self.unary.mutate(mate_pool[i],self.random)
                self.pop[i] = pcur

            fitness_scores.append(self.pbest.y)
        return fitness_scores,self.pbest

def main():
    fitness_scores = list()
    best_founded_solution = Individual()
    max_semesters = inputs.get_max_terms()
    course_numbers = inputs.get_courses_nums()
    gpm = GPM()
    nullary = Nullary(cnum=course_numbers,max_semester_num=max_semesters)
    unary = MPX(max_semester_numbers=max_semesters)
    binary= UCX()
    selection = Tournament()
    termination = MaxTimeTermination(10)
    objective = WeightedObjective()
    pop_size = 4
    cr = 0.7
    genetic = GE(random=random,gpm=gpm,nullary=nullary,unary=unary,binary=binary,selection=selection,termination=termination,pop_size=pop_size,cr=cr)
    fitness_scores,best_founded_solution = genetic.solve(objective=objective)
    print(best_founded_solution)
    plot_results(fitness_scores)

if __name__ == "__main__":
    main()