from individual import Individual
import random
import math
from plot_results import plot_results
class SimulatedAnnealing:
    def __init__(self,random,temp_schedular,gpm,nullary,unary,termination):
        self.tabu_list=list()
        self.gpm = gpm
        self.nullary = nullary
        self.unary = unary
        self.termination = termination
        self.p_best = Individual()
        self.time_index=0
        self.temp_schedular=temp_schedular
        self.random=random
    def solve(self,objective):
        fitness_scores = list()
        self.p_best.g = self.nullary.create(self.random)
        self.p_best.x = self.gpm.gpm(self.p_best.g)
        self.p_best.y = objective.compute(self.p_best.x)
        p_current = self.p_best 
        self.time_index = 1
        while (self.termination.shouldTerminate() == False):
            p_new = Individual()
            p_new.g = self.unary.mutate(self.random,p_current.g,4)
            p_new.x = self.gpm.gpm(p_new.g)
            p_new.y = objective.compute(p_new.x)
            delta_e = p_new.y - p_current.y
            if (delta_e<=0):
                p_current = p_new
                if (p_current.y < self.p_best.y):
                    self.p_best = p_current
            else:
                T = self.temp_schedular.get_temperature(self.time_index)
                if (random.random() < math.exp(-delta_e/T)):
                    p_current = p_new
            fitness_scores.append(self.p_best.y)
            # print(fitness_scores)
            self.time_index+=1
        plot_results(fitness_scores)
        return self.p_best