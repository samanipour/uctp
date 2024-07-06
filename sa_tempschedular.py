import math
class TempSchedular:
    # define an Interface for Temperature Schedular
    def get_temperature(self,time_index):
        pass

class LnTempSchedular(TempSchedular):
    def __init__(self,t_start):
        self.t_start = t_start
    def get_temperature(self,time_index):
        if (time_index < 3):
            return self.t_start
        else:
            return (self.t_start/math.log(time_index))
        
class PolyTempSchedular(TempSchedular):
    def __init__(self,t_start,epsilon):
        self.t_start = t_start
        self.epsilon = epsilon
    def get_temperature(self,time_index):
        return (math.pow((1-self.epsilon),time_index)*self.t_start)