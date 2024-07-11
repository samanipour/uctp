import time

class MaxTimeTermination:
    def __init__(self,max_time):
        self.max_time = max_time
        self.start_time = 0
        self.current_time=0
    def shouldTerminate(self)->bool:
        global start_time
        global current_time
        if (self.start_time == 0):
            self.start_time = time.time()
        self.current_time = time.time()
        if (self.current_time-self.start_time >= self.max_time):
            return True
        else:
            return False