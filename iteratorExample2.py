# '''
# Iterator Example
# '''

class RemoteControl(object):
    def __init__(self):
        self.channel = ['HBO','ESPN','ZEE','DDSports']
        self.index = -1
        
        
    
    
    def __iter__(self):
        return self
        

    def __next__(self):
        try:
            self.index+=1
            if(self.index>=len(self.channel)):
                raise StopIteration
            return self.channel[self.index]
        except StopIteration as e:
            print(e())
            




r= RemoteControl()

itr = iter(r)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

