class odd_even:
    def check(self,num):
        if num%2==0:
            print(num,"is even number")
        else:
            print(num,"is odd number")

n=odd_even()
x = int(input("enter a value:"))
n.check(x)