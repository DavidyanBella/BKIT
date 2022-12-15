import time

class Cm_timer_1:
    
    def __init__(self):
        self.result = 0


    def __enter__(self):
        self.start_time = time.time()
        return "cm_timer_1"

    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            self.end_time = time.time()
            self.result = self.end_time - self.start_time
            print("time:", self.result)

