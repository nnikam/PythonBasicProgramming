from abc import ABCMeta,abstractmethod
'''

    1.Interface in python
    2.Use of metclass in python
    3.use of abstract method in python
'''

class Shape(metaclass=ABCMeta):
    

    @abstractmethod    
    def area():pass

    @abstractmethod
    def perimeter():pass

class Rectange(Shape):
    
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.height*self.width
        
    def perimeter(self):
        return self.height*2+self.width*2
        
    



s=Rectange(5,6)

#print(dir(s.__class__))
print("The Area of {0} is {1}".format(type(s).__name__,int(s.area())))
print("The Perimeter of {0} is {1}".format(type(s).__name__,int(s.perimeter())))
