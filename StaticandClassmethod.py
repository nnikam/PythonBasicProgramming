class Employee(object):
    companyName=None

    def __init__(self,fname,lname):
        self.fname = fname 
        self.lname = lname
        print("Object Created Successfully")
        
        
    @classmethod    
    def from_string(cls,value):
        print("inside class method")
        fname,lname = value.split('-')
        return cls(fname,lname)
        
    @staticmethod    
    def CompanyName(companyvalue):
       print("The Company name is"+companyvalue)
        
        
    def printEmployee(self):
        print("Hey my full name is {0}.{1}".format(self.fname,self.lname))
        
        


e1=Employee('nitin','nikam')
e1.printEmployee()
        
e2= Employee.from_string("Poonam-Tumma")
e2.printEmployee()

Employee.CompanyName("Cummins")





        





