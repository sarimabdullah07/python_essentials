def deco(admission):
    def wrapper(*args):
        admission(*args)
        print("Thank you!")
    return wrapper
@deco
def new_admit(name,age):
    print("Name = ",name)
    print("Age = ",age)
new_admit("Sarim",100)
