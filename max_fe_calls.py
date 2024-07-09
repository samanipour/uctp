class MaxFeCalls:
    def __init__(self,max_fe_calls):
        self.max_fe_calls = max_fe_calls
        self.number_of_calls = 0
    def shouldTerminate(self)->bool:
        # global number_of_calls
        self.number_of_calls +=1
        if (self.number_of_calls >= self.max_fe_calls):
            return True
        else:
            return False