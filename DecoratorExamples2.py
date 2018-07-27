import time

class DecoratorExample(object):
    
    def __init__(self,method):
        self.method = method

    def __call__(self,*args,**kwargs):
        print("Using Class level decorator")
        start = time.time()
        self.method(*args,**kwargs)
        end = time.time()
        print("Total time is "+str(end-start))
        

def time_decorator(myfunc):
    def wrapper(*args,**kwargs):
        start = time.time()
        myfunc(*args,**kwargs)
        end = time.time()
        print("Total time is "+str(end-start))
    return wrapper
        

def fancy_Decorator(myfunc):
    def wrapper(*args,**kwargs):
        print("**********")
        myfunc(*args,**kwargs)
        print("***********")
    return wrapper

@DecoratorExample
def Squares(nums):
    L = [ item*item for item in nums]
    print("The Square result is"+str(L))

    
# @fancy_Decorator    
# @time_decorator
# def Cubes(nums):
#     L = [ item*item*item for item in nums]
#     print("The Cube result is"+str(L))




Squares(range(5))
#Cubes(range(5))