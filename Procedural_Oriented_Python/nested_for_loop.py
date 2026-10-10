print("Right Angled Triangle")
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()

print("Inverted Right Angled Triangle")
for a in range(5,0,-1):
    for b in range(a):
        print("*",end=" ")
    print()

print("Pyramid")
for c in range(1,6):
    for z in range(5-c):
        print(" ",end="")
    for y in range(c):
        print("* ",end="")
    print()

print("Diamond")
for d in range(1,6):
    print(" "*(5-d)+"* "*(d))
for e in range(1,6):
    print(" "*(e)+"* "*(5-e))

print("Number Triangle")
for f in range(1,6):
    for g in range(f):
        print(g,end=" ")
    print()

print("Same num per row traingle")
for ab in range(1,6):
    for ba in range(1,ab+1):
        print(ab-1,end=" ")
    print()

print("Floyd's Triangle")
h=0
for k in range(1,6):
    for l in range(k):
        h+=1
        print(h,end=" ")
    print()
