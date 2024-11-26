class student:
    def method(self):
        print("i am a method")
        print("i was called using",id(self))

s1=student()
s2=student()
print("id so s1=",id(s1))
print("id of s2",id(s2))
s1.method()
s2.method()