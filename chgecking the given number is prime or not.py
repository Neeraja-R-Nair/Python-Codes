n=int(input("enter a number"))
c=0
for i in range(2,n//2):
    if(n%i==0):
        print(n,"not a prime")
        c=c+1;
        break
if(c==0):
    print(n,"is a prime")