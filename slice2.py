"""s='karthi'
output=s[0].upper() + s[1:]
print(output)"""

#covert last letter of string into upper case string

s="karthi"
output= s[0:len(s)-1]+s[-1].upper()
print(output)