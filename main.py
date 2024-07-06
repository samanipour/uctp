import random
import math
from individual import Individual
from gpm import gpm
from objective import compute
from course import Course
from student import Student
from instructor import Instructor

from tournament import select
from ux import recombine
from multimutate import mutate
import inputs
from plot_results import plot_results

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
pbest.y = math.inf
mate_pool = list()
mate_size = pop_size
cr = 0.7
student_list = inputs.get_students()
instructor_list = inputs.get_instructors()
course_list = inputs.get_uni_programs()[0].courses #TODO: should consider all program courses
uni_programs =inputs.get_uni_programs()
fitness_scores = list()
while (t < 10000):
    for i in range(pop_size):
        pcur = pop[i]
        pcur.x = gpm(pcur.g,max_semester_num)
        pcur.y = compute(pcur.x,instructor_list=instructor_list,course_list=course_list,student_list=student_list,
                         uni_programs=uni_programs,min_load=12,max_load=24,random=random)
        
        if (pcur.y<pbest.y):
            pbest = pcur

    mate_pool = select(pop,3,random)
    for i in range(mate_size):
        pcur = Individual()
        if (random.random() < cr):
            j = random.randint(0,mate_size-1)
            pcur = recombine(mate_pool[i],mate_pool[j],random)
        else:
            pcur = mutate(mate_pool[i],max_semester_num,random)
        pop[i] = pcur
    t+=1
    fitness_scores.append(pbest.y)
plot_results(fitness_scores)