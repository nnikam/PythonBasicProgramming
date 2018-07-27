import os 
from contextlib import contextmanager 


#ContextManager example1
#this is modified file of the context manager
@contextmanager
def open_file(destination,mode):
    try:
        f = open(destination,mode)
        yield f 
    finally :
        f.close()
        
        


with open_file('Test.txt','r') as f:
    print(f.read())
    
print(f.closed)






   
