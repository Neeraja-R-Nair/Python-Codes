class student:
    studcount = 5 #class attributes
    def __init__(self,name):
        self.name = name #instance attributes

s1=student("Neeraja")
print(student.studcount)#refers to class member
print(s1.studcount)#refers to class member
s1.studcount = 10 #creates instance member
print(s1.studcount)#refers to instance member
print(student.studcount)