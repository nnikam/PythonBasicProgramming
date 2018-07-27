class Myclass(object):
    def __init__(self):
        self.__x =None #this is Private variable 
        self.__y=None  #this is Private variable
        self._z = None # this is protected
        
    @property    
    def x(self):
        print("inside getter function")
        return self.__x
    
    @x.setter    
    def x(self,value):
        print("inside setter function")
        self.__x = value
        
    @x.deleter   
    def x(self):
        print("inside deleter function")
        self.__x = None
        
    @property    
    def y(self):
        print("inside getter function")
        return self.__y
    
    @y.setter    
    def y(self,value):
        print("inside setter function")
        self.__y = value
        
    @property    
    def z(self):
        print("inside getter function")
        return self._z
    
    @z.setter    
    def z(self,value):
        print("inside setter function")
        self._z = value
    
   
 

 
        
        
        

obj = Myclass()
#this will call seter method mautomatically
obj.x=10
print(obj.x)
#This will not setter method
obj._Myclass__x=55
print(obj._Myclass__x)

print("******************************")


print("-----------------------------")
obj.z = 50
print(obj.z)
print(obj._z)
print("-----------------------------")
#del obj.x
#This is how you can access private variable in python

#print("Value of X is {}".format(obj._Myclass.__x))

