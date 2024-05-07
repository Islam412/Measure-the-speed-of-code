
import time


def caculater_time(func):
    def inner(a,b):
        
        start = time.time()
        
        result=func(a,b)
        
        end = time.time()
        
        print(f'total time : {end-start}')
        return result
        
    return inner


@caculater_time
def mysum(x,y):
    time.sleep(5)
    return x+y
    
mysum(3,4)