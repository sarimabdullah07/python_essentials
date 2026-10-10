import functools

# Syntax: map(function,collection)
z=(lambda a:0 if a%2==0 else 1)
a=([23,45,62,98,34,55,97,12])
print(list(map(z,a)))

# Syntax: filter(function,collection)  
b=(["Majid","Abdullah","Salmaan","Sajid","kaleemurrahman","Hamid","Shahid","Ali","Wahid","Khalid","Aabid","Rashid"])
y=lambda a:len(a)==5 or len(a)==6
print(list(filter(y,b)))

# Syntax: reduce(function,collection)
c=([48,32,12,67,89,34,56,62])
x=(lambda a,b:a if a>b else b)
print(functools.reduce(x,c))