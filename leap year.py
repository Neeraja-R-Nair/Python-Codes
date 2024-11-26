year=int(input("Enter a year : "))
if year%100==0:
    if year%400==0:
        print("LEAP YEAR")
    else:
        print("NOT LEAP YEAR")

else:
    if year%4==0:
        print("LEAP YEAR")
    else:
        print("NOT LEAP YEAR")