class myiter(object):
    
    def __init__(self,start,end):
        self.start = start
        self.end = end 
        
    
    def __iter__(self):
        return self
        
    
    def __next__(self):
        if(not(self.start>=self.end)):
            self.start+=1
            return self.start
        else:
             raise StopIteration
             
             


m = myiter(5,10)

print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))


            

