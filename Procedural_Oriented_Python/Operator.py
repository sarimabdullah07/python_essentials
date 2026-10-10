print("\nArithmetic")
a=int(input("Enter 1st number: "))
o=(input("Enter Operator: "))
b=int(input("Enter 2nd number: "))
match o:
    case '+':
        print("Ans= ",a+b)
    case '-':
        print("Ans= ",a-b)
    case '*':
        print("Ans= ",a*b)
    case '/':
        print("Ans= ",a/b)
    case '%':
        print("Ans= ",a%b)
    case '//':
        print("Ans= ",a//b)
    case '**':
        print("Ans= ",a**b)

print("\nComparision")
c=int(input("Enter first number: "))
d=int(input("Enter second number: "))
print(f"{c}=={d}={c==d}")
print(f"{c}!={d}={c!=d}")
print(f"{c}>{d}={c>d}")
print(f"{c}>={d}={c>=d}")
print(f"{c}<{d}={c<d}")
print(f"{c}<={d}={c<=d}")

print("\nAssignment")
e=int(input("Enter first number: "))
f=int(input("Enter second number: "))
e+=f
print(f"e+=f : {e}")
e-=f
print(f"e-=f : {e}")
e*=f
print(f"e*=f : {e}")
e/=f
print(f"e/=f : {e}")
print("Assignment Operators: =, +=, -=, *=, /=, %=, //=, **=")

print("\nLogical Operator")
g=int(input("Enter first num: "))
h=int(input("Enter second num: "))
z=input("Enter logic (and,or,not): ")
print(f"{g}=={h} --> {g==h}\n{g}!={h} --> {g!=h}")
match z:
    case 'and':
        print(f"{g}=={h} and {g}=={h}: {(g==h) and (g==h)}")
        print(f"{g}=={h} and {g}!={h}: {(g==h) and (g!=h)}")
        print(f"{g}!={h} and {g}=={h}: {(g!=h) and (g==h)}")
        print(f"{g}!={h} and {g}!={h}: {(g!=h) and (g!=h)}")
    case 'or':
        print(f"{g}=={h} or {g}=={h}: {(g==h) or (g==h)}")
        print(f"{g}=={h} or {g}!={h}: {(g==h) or (g!=h)}")
        print(f"{g}!={h} or {g}=={h}: {(g!=h) or (g==h)}")
        print(f"{g}!={h} or {g}!={h}: {(g!=h) or (g!=h)}")
    case 'not':
        print(f"not {g}=={h}: {not (g==h)}")
        print(f"not {g}!={h}: {not (g!=h)}")

print("\nBitwise")
i=int(input("Enter 1st num: "))
j=int(input("Enter 1st num: "))
print(f"{i}&{j}={i&j}")
print(f"{i}|{j}={i|j}")
print(f"~{i}={~i}")
print(f"~{j}={~j}")
print(f"{i}^{j}={i^j}")
print(f"{i}>>{j}={i>>j}")
print(f"{i}<<{j}={i<<j}")

print("\nIdentity")
k=int(input("Enter 1st num: "))
l=int(input("Enter 2nd num: "))
print(f"{k} is {l} : {k is l}")
print(f"{k} is not {l} : {k is not l}")

print("\nMembership")
list=[10,20,30,40,50,60]
print(list)
m=int(input("Enter number to search in the given list: "))
print(f"{m} in list: {m in list}")
print(f"{m} not in list: {m not in list}")
