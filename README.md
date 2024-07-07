Optimization Course Project:

The goal of this project is to use meta-heuristics algorithms and present optimization software for course scheduling at University. The detailed description of the problem is as follows:

[The final objective is to provide a program that specifies which courses should be offered by which professor each semester and which courses each student should take in each semester]

[The faculty has several specific curricula that specify which courses students must take and which courses they can take as electives. Therefore, the curricula of the faculty are inputs to the problem, indicating which courses are mandatory and which are elective, along with the prerequisites and co-requisites for each course. Each student has a specific curriculum and must take courses according to it. There are also common courses among different curricula. In each curriculum, it is specified how many mandatory and elective load must be completed. These constraints must be maintained]

[The priority for offering courses is determined by the capability of the Instructor. Each professor has a list of courses they can teach, rated on a scale from 1 to 10, where 1 is the highest priority and 10 is the lowest. Higher priority indicates a higher preference for teaching the course. Multiple courses can have the same priority. The better schedule is one in which higher-priority courses are offered to the Instructor]

[Some professors are visiting faculty who do not have a mandatory teaching load. The fewer credits assigned to these visiting professors, the better the scheduling.]

[The more students in a class, the better the scheduling is considered to be (the fewer total credits offered by the faculty, the better). Each professor has a mandatory teaching load each semester, and the closer the professor's assigned credits are to this mandatory load, the better the scheduling. Each course has a specified number of credits, which is indicated in the course information]

[Each course has a certain number of load, and information about each course specifies whether it is for undergraduate, master's, or doctoral students. master's and doctoral course counts as 1.5 load for a professor. common course between two programs counts once.]

[Students have a maximum and minimum number of loads they can take each semester. The ideal schedule would balance the number of loads across all semesters, except for the final semester, where the number of load should be minimized as much as possible.]