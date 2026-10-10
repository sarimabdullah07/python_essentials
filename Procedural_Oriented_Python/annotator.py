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


def trigno(math):
    def wrapper(*arg,**kwarg):
        print(len(arg))
        print("sin")
        math(*arg,**kwarg)
    return wrapper

@trigno
def angle(c,t,b="B",a="A"):
    print(c)
    print(t)
    print(a)
    print(b)
angle("cos","tan",a="alpha",b="beta")
