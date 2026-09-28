global_variable="Good Morning"
# global_variable is accessable to every where
def greeting():
    local_variable="Hi alice! "
    print(local_variable)
    # local_variable is accessable only in the function
    print(global_variable)

greeting()
print("Global-->",global_variable) #we can access the golobal variable inside or outside the function 
# print(local_variable) --> it generate error bcz it only accessable in the function

vehical="car"
def car_apperence():
    name="bugatti"
    colour="white"
    i=1
    print(name,vehical,"is",colour,"in colour") # global + local variable
    def car_price():
        nonlocal i
        i+=1
        print(i)
        price="1.2 million $"
        print(name,"price is",price) #child function can access it's own variable as well as parent's variable
    car_price()  
    # print(price) --> but parent function is not able to access the variable of child function  
car_apperence()
