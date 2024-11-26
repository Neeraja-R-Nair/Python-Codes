def convert_km_to_miles(km):
    miles = km *0.621371
    return miles
km=float(input("enter distance in kilometers:"))
miles=convert_km_to_miles(km)
print(f"kilometers is equal to {miles:2f}miles.")