class student:
    mark1,mark2,mark3=45,91,71  #class variable
    def process(self): #class method
        sum=student.mark1 + student.mark2 + student.mark3
        avg = sum/3
        print("total marks =",sum)
        print("average marks=",avg)
        return
    
s=student()
s.process()