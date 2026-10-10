#Output
print("This is my Output.")

#Input 
a=input("Enter string: ")
#formate Specifier
print(f"Data type of input is {type(a)}")

b=int(input("Enter a number: "))
print(f"Data type of input is {type(b)}")

c=float(input("Enter Decimal value: "))
print(f"Data type of input is {type(c)}")

#Map function
d,e,f,g,h=map(int,input("Enter 5 numbers: ").split())
print(f"multi input: {d,e,f,g,h}")