#user defined error handling

class xyz(Exception):
    def __init__(self, x,msg):
        self.x=x
        self.msg=msg
    def __str__(self):
        return f"{self.x} : {self.msg}"

try:
    age=int(input("Enter age: "))
    if 18>age or 59<age:
        raise xyz(age,"Age should be in between 18 to 59")
except xyz as x:
    print(x)
else: 
    print("You are ELigible for Teaching")

