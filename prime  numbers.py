n=int(input("enter a number"))
for i in range(2,n//2):
    if(n%i==0):
        print(n,"not a prime")
        break
    else:
        print(n,"is a prime")
        break
    