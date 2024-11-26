def swap_with_temp(x,y):
    temp=x
    x=y
    y=temp
    return x,y


x,y=swap_with_temp(5,10)
print( f"x={x},y={y}")