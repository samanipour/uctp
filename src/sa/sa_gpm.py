class GPM:
    def __init__(self,max_msems):
        self.max_semester=max_msems
    def gpm(self,g):
        semesters = list()
        for i in range(1,self.max_semester+1):
            sem = [j for j in range(len(g)) if i == g[j]]
            semesters.append(sem)
        return semesters