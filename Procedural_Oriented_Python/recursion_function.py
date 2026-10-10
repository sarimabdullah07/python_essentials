#recursion function fibonacci series
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        f=fibonacci(n-1)+fibonacci(n-2)
    return f
l=int(input("Enter number of terms for fibonacci series: "))
for i in range(l):
    print(fibonacci(i),end=" ")

#factorial of a number
def fact(n):
    if n==1:
        return 1
    else:
        factorial=fact(n-1)*n
    return factorial
j=int(input("\nEnter a number: "))
print("factorial of",j,"=",fact(j))