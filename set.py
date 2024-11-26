#SET
s={10,20,30,40,50,60}
s.add(70)
print(s)
s.remove(40)
print(s)


#how to create empty set
s=set()
print(type(s))
print(s)

#FROZEN SET
s={10,20,30}
fs= frozenset(s)
print(type(fs))
fs.add(50) #we cant add or remove elements in frozen set