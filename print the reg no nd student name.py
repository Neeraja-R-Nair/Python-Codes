class student:
    student_count=0
    def __init__(self,name):
        student.student_count +=1
        self.regno=student.student_count
        self.name=name
    def __str__(self):
        return str(self.regno) + " " + self.name
s1=student(" jersey ")
s2=student(" tom ")
print(s1)
print(s2) 