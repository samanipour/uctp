from individual import Individual
import random
# random.seed(141)
def recombine(p1,p2,random):
    chromosom_size = len(p1.g)

    ofs1 = Individual()
    ofs2 = Individual()
    ofs1.g = [-1]*chromosom_size
    ofs2.g = [-1]*chromosom_size

    start, end = sorted([random.randrange(chromosom_size) for _ in range(2)])
    ofs1.g[start:end + 1] = p1.g[start:end + 1]
    ofs2.g[start:end + 1] = p2.g[start:end + 1]

    p2_index = 0
    for i in range(chromosom_size):
        if ofs1.g[i] == -1:
            while (p2.g[p2_index] in ofs1.g):
                p2_index += 1
            ofs1.g[i]= p2.g[p2_index]
    # # Fill remaining positions with entries from the other parent
    # for i in range(chromosom_size):
    #     if i < start or i > end:
    #         # Avoid repetitions
    #         if p1.g[i] not in ofs1.g:
    #             ofs1.g[i] = p1.g[i]
    #         if p2.g[i] not in ofs2.g:
    #             ofs2.g[i] = p2.g[i]

    return ofs1