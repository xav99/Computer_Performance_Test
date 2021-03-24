'''
Xavier 
1/03/2020
'''
import time
from variable_info import getFuncName

def timer(func):  # Gives us the execution time of a function
    def decorate(*args, **kwargs):
        start = time.time()
        x = func(*args, **kwargs)
        total = time.time() - start
        print(getFuncName(func),"took:", total, "seconds to execute")

    return decorate() # this can be used to test computer speeds?


'''   
@timer  # decorator usage example     
def rgb():
    for _ in range(1000000):
        pass
'''
