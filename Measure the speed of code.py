import time


def caculater_time(func):
    
    def inner(*args,**kwargs):
        
        print('start ....')
        func(*args,**kwargs)
        print('end ...')
        
    return inner()


