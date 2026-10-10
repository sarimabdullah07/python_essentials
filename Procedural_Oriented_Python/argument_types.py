# positional argument
def result(name,roll_no,marks):
    print("Name: ",name,"\nRoll number: ",roll_no,"\nPercentage: ",round(sum(marks)/len(marks),2))
result("Sarim",1704,[94,89,92,87,88,97])
'''
we cannot change the position of arguments while calling a function.
'''

# keyworded argument
def result(name,roll_no,marks):
    print("\nName: ",name,"\nRoll number: ",roll_no,"\nPercentage: ",round(sum(marks)/len(marks),2))
result(roll_no=624,marks=[94,89,92,87,88,97],name="Abdullah")
'''
we can assign keywords to the functions while calling,
we can change the position of arguments by using keywords,
note: The keywords should match the actual argument (parameter) names
'''

#default argument
def greet(name, a="assalamualikum"):
    print(name)
    print(a)
greet("\n sarim")
'''
If you omit these arguments during a function call,
python uses the default value. If you pass a value, it overrides
the default
'''

# arbitrary positional argument
def area_of_circle(*marks):
    total=sum(marks)
    print("\n",marks,"\n","Total_Marks= ",total)
area_of_circle(23,55,76,87,90)
'''
Prefixed with a single asterisk(*), this collects any number
of extra positional arguments into a sinngle tuple.
'''

# arbitrary keyword argument
def info(**data):
    print("\n",data)
info(roll_no=812,marks=872,percentage=93.47)
'''
Prefixed with a double asterisk(**), this collects any number
of extra keyword arguments into a standard dictionary
'''

# positional + arbitray keyword arguments 
def info(name,**data):
    print("\n",name," = ",data)
info("Sarim",roll_no=812,marks=872,percentage=93.47)

# positional + arbitray posional arguments (*args)
def info(box_num,*fruit):
    print("\n",box_num," = ",fruit)
info(107,"Apple","Mango","Dates","Orange")


# positional + default argument
def just(name,city="malegaon"):
    print("\nHi! ",name)
    print("Are you from,", city,"?")
just("Abdullah")
just("Aqueel","Mumbai")
'''
A mix where optional parameters are assigned a fallback value using the assignment
operator(=). Required parameters must occupy the left side. Optional default parameters 
must occupy the right side.
'''

# The Complete Mix
def all(name,*marks,**mws):
    print("\nName: ",name)
    print("marks: ",marks, "\nPercentage= ",(sum(marks)/len(marks)))
    print("marks with subject: ",mws)
all("abdurrahman",87,96,89,79,92,english=87,math=96,chemistry=89,biology=79,physices=92)
'''
The standard sequencing structure required when mixing all three types. 
Python strictly requires this order: fixed positional then (*args) and at last (**kwargs).
'''