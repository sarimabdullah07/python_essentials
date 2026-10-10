#table
n=int(input("Enter a number to print mathametical table: "))
for i in range(1,11):
    print(f"{i} x {n} = {i*n}")

#even numbers
for j in range(0,51,2):
    print(j,end=" ")

#for loop in list
list=["apple","banana","mango","kiwi","papaya"]
print(list)
s=input("Enter fruit name: ")
for i in list:
    if(s in list):
        print("Available")
        break
    else:
        print("Not Available")
        break

