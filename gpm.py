def gpm(g,max_semester):
    semesters = list()
    for i in range(1,max_semester+1):
        sem = [j for j in range(len(g)) if i == g[j]]
        semesters.append(sem)
    return semesters