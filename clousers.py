
def math():
    i=10
    def inner():
        j=20
        return i+j
    return inner
a=math()
print(a())

def outer():
    i="Welcome to python"
    def inner():
        j="Hi! "
        return j+i
    return inner
var=outer()
print(var())

def make_counter():
    count=0
    def increment():
        nonlocal count
        count+=1
        return count
    return increment
my_counter=make_counter()

print(my_counter())
print(my_counter())