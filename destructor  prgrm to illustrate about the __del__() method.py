class sample:
    num=0
    def __init__(self,var):
        sample.num+=1
        print("objects value is =",var)
        print("the value of class variable is=",sample.num)
    def __del__(self):
        sample.num-=1
        print("objects with the value %d is exit from the scope"%self.var)

s1=sample(15)
s2=sample(35)
del s1
del s2