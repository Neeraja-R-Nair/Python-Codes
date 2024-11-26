class example:
    def __init__(self,a,b): #constructor
        self.a = a 
        self.b = b 
    def add(self): #function
        return self.a + self.b
e = example(8,6) #pass arg
print(e.add()) #14