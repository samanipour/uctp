import math
import numpy as np

class Nullary:
    def __init__(self,cnum,max_semester_num):
        self.cnum = cnum
        self.max_semester_num=max_semester_num
    def create(self,random):
        # sol = Individual()
        g = [-1] * self.cnum #chromosome size
        for i in range(self.cnum):
            random_sem = random.randint(1,self.max_semester_num)
            g[i] = random_sem
        return g

def main():
    pass

if __name__=="__main__":
    main()