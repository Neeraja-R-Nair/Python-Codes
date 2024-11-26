n=int(input("enter a number"))
armstrong=0
n1=n
while(n>0):
    num=n%10
    armstrong=armstrong+num**3
    n=n//10
if(armstrong==n1):
    print(n1,"is a armstrong number")
else:
    print(n1,"not an armstrong number")
