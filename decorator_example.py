'''
function()-----------------------------------> decorator(1)
    print("Welcome to dark web")
___________________________________________________________________________________________________________
Enter email: alpha123@gmail.com
if email==true_email: -----------------------> main_function
    var=print("Enter passward")
    if passward==true passward:
        function() -------------------------> decorator(1)
        new_function()----------------------> decorator(2)
    else
        ("Chal nikal!..")
else 
    print("Incorrect email")
_____________________________________________________________________________________________________
new_function()------------------------------> decorator(2)
    print("Don't do any illegal work here")
'''

def main():
    def wrapper():
        email=input("Enter email: ")
        true_email="alpha123@gmail.com"
        if email==true_email:
            true_passward=int("011026")
            passward=int(input("Enter passward: "))
            if passward==true_passward:
                deco_1()
                # decorator_2()
                pass
        else:
            print("Incorrect email")
    return wrapper

@main
def deco_1():
    print("Welcome to dark web...")
deco_1()