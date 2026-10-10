import math
print((lambda a:math.sqrt(a)+a**2)(25))
print((lambda a,b,c:a if a>b>c else(b if b>a>c else c))(82,43,98))
print(list(map((lambda a:0 if a%2==0 else 1),([32,45,23,60,12,57]))))
print((lambda a: "verified" if a==2190 else "Incorrect passward")(2190))
print((lambda a:a.upper())("python"))
print("Tickect Price:",(lambda a: 10 if a<=10 else (20 if a<=20 else 25))(23))
print((lambda a:"Eligible to vote" if a>=18 else "Not eligible")(19))
print((lambda a: sum(a)/len(a))([76,85,82,93,72]))