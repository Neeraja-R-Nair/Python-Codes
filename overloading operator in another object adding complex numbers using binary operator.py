class complex_1:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,u):
        return self.x + u.x, self.y + u.y
    
object_1 = complex_1(23,12)
object_2 = complex_1(21,22)
object_3 = object_1 + object_2
print(object_3)