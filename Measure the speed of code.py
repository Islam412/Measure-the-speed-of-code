# import time


# def caculater_time(func):
#     def inner(a,b):
        
#         print('start ....')
#         result=func(a,b)
#         print('end ...')
#         return result
        
#     return inner


# @caculater_time
# def mysum(x,y):
#     print(x+y)
    
# mysum(3,4)



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