Optimization Course Project:

The goal of this project is to use meta-heuristics algorithms and present optimization software for course scheduling at University. The detailed description of the problem is as follows:

    The final objective is to provide a program that specifies which courses should be offered by which professor each semester and which courses each student should take in each semester. The priority for offering courses is determined by the capability of the Instructor. Each professor has a list of courses they can teach, rated on a scale from 1 to 10, where 1 is the highest priority and 10 is the lowest. Higher priority indicates a higher preference for teaching the course. Multiple courses can have the same priority.

    The better schedule is one in which higher-priority courses are offered to the Instructor. The program must determine which mandatory and elective courses each student should take. The input to the problem includes a specific list of mandatory and elective courses for each student, as well as the prerequisites and co-requisites for each course.
    
    type 2 Instructor don't have predefined loads, for these type it's better to assign theme course as low as possible course that their total loads be minimize

    Students have a maximum and minimum number of loads they can take each semester. The ideal schedule would balance the number of loads across all semesters, except for the final semester, where the number of load should be minimized as much as possible.

    Each course has a certain number of load, and information about each course specifies whether it is for undergraduate, master's, or doctoral students. For example, a master's course counts as 1.5 load for a professor. common course between two programs counts once.

    The faculty has several specific curricula that specify which courses students must take and which courses they can take as electives. Therefore, the curricula of the faculty are inputs to the problem, indicating which courses are mandatory and which are elective, along with the prerequisites and co-requisites for each course. Each student has a specific curriculum and must take courses according to it. There are also common courses among different curricula. In each curriculum, it is specified how many mandatory and elective load must be completed. These constraints must be maintained.

    A better schedule would minimize the difference between the assigned load and the mandatory load for each professor. The closer the assigned credits are to the mandatory credits, the better the schedule.


    The program should input the problem data as a file and output the optimized schedule in a specific format.