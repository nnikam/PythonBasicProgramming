class Employee(object):
    
    def __init__(self,fname,lname,gender):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        
        
    def displayfullname(self):
        print("The Full name is =>{0} and his gender is {1}".format((self.fname+self.lname),self.gender))
        
        


class Programmer(Employee):
    
    def __init__(self,fname,lname,gender,language):
        #Employee.__init__(self,fname,lname,gender)
        super(Programmer,self).__init__(fname,lname,gender)
        self.language = language
        
        
        
    def displayLanguage(self):
        print("The Language of Programmer is {0}".format(self.language))
        
    
    def displayfullname(self):
        print ("Hey i am inside the Class ")




p = Programmer('nitin','nikam','male','Java')
p.displayfullname()
p.displayLanguage()


e =Employee('Saurav','Dhamapurkar','Male')
e.displayfullname()

#print(p.__name__)
#print(help(Programmer))





