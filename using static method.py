class calculator:
    def addnumbers(x,y) :
        return x+y
    
#create addnumbersstatic method
calculator.addnumbers=staticmethod(calculator.addnumbers)
print('sum:',calculator.addnumbers(15,110)) #125