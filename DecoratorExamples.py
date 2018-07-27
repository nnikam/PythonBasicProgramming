'''
1.Function decorator
2.Class level decorator
'''
import time


def Decortor_function(original_function):
    def wrapper_function(*args,**kwargs):
        t1=time.time()
        original_function(*args,**kwargs)
        t2=time.time()
        print("The total time is {0} sec".format(str(t2-t1)))  
    return wrapper_function
    
    
def fancy_decorator(original_function):
    def wrapper_function(*args,**kwargs):
        print("***********")
        original_function(*args,**kwargs)
        print("*************")
    return wrapper_function
    
    
    

class Class_Decorator(object):
    
    def __init__(self,original_function):
        self.original_function = original_function
        
        
    def __call__(self,*args,**kwargs):
        print("Inside Class Decorator")
        t1=time.time()
        self.original_function(*args,**kwargs)
        t2=time.time()
        print("The total time is {0} sec".format(str(t2-t1)))  
        
        
        
        
        



@fancy_decorator
@Decortor_function
def Add(a,b):
    print("The Addition is"+str(a+b))
    
    
@fancy_decorator
@Decortor_function
def Sub(a,b):
    
    print("The Subtraction is"+str(a-b))




Add(10,20)
Sub(30,20)





