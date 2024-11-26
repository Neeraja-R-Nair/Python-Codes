class example:
    def __init__(self,x):
        self.x=x
    def __add__(self,u):
        return self>x +u.x
object_1=example(int(input(print("enter the value:"))))
object_2=example(int(input(print("enter the value:"))))
print(":",object_1 + object_2)
object_3=example(str(input(print("enter the value:"))))
object_4=example(str(input(print("enter the value:"))))
print(":",object_3 + object_4)