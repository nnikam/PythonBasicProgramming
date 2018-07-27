
class MathTest(object):
    """
        This is the sample class for doing basisc mathematic operation
    """
    def __init__(self,a,b):
        self.a = a 
        self.b = b

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def mul(self):
        return self.a*self.b



m= MathTest(20,10)
print(m.add())
print(m.sub())


