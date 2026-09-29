def pre_deco():
    print("Hi! ")

def post_deco():
    print("Bye")

def main(var1,var2):
    def encapsulation():
        var1()
        print("Welcome to python decorator")
        var2()
    return encapsulation

x=main(pre_deco,post_deco)
x()
#----------------------------------------------------------------

def pre():
    print("hello!")

def post():
    print("I am fine")

def main(f1,f2):
    f1()
    print("How are you?")
    f2()

main(pre,post)
