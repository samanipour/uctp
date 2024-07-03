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

snum = 300
cnum = 10
inum = 4
max_semester_num = 4
ins_min_load = 3
ins_max_load = 24
course_list = list()
for i in range(cnum):
    c = Course(i)
    course_list.append(c)
# print(course_list[0])

instructor_list = inputs.get_instructors()
# print(instructor_list)
# genetic algo
pop_size = 4

sol = Individual()
sol.g = [-1] * cnum #chromosome size
pop = list()
# random.seed(1403)
# init pop
for i in range(pop_size):
    sol = Individual()
    sol.g = [-1] * cnum #chromosome size
    for i in range(cnum):
        random_sem = random.randint(1,max_semester_num)
        sol.g[i] = random_sem
    pop.append(sol)

# print(pop[0].g)
# plan = gpm(pop[0].g,max_semester_num)
# print (plan)
# print(">>>>>>>>>>>>>>>>")
t=0
pbest = Individual()
pcur = Individual()
pbest.y = math.inf
mate_pool = list()
mate_size = pop_size
cr = 0.7
while (t < 100):
    for i in range(pop_size):
        pcur = pop[i]
        pcur.x = gpm(pcur.g,max_semester_num)
        pcur.y = compute(pcur.x,instructor_list,course_list,random)
        
        if (pcur.y<pbest.y):
            print(pcur)
            pbest = pcur
            # print("<<")

    mate_pool = select(pop,3,random)
    # print(mate_pool)
    # print(">>>>>>>>>>>>>>")
    for i in range(mate_size):
        pcur = Individual()
        if (random.random() < cr):
            j = random.randint(0,mate_size-1)
            pcur = recombine(mate_pool[i],mate_pool[j],random)
        else:
            pcur = mutate(mate_pool[i],max_semester_num,random)
        pop[i] = pcur
    t+=1
    # print(pbest)