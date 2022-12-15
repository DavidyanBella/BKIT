from contextlib import contextmanager
from time import time

@contextmanager
def Cm_timer_2():
    start_time = time()
    yield "cm_timer_2"
    print("time:", time() - start_time)
