class Student:
    def __init__(self,roll_no,name,marks):
        self.roll_no=roll_no
        self.name=name
        self.marks=marks
        print("This is constructor")

    def display(self):
        print(self.name)
        print(self.roll_no)
        print(sum(self.marks))
        print(sum(self.marks)/len(self.marks))

class staff:
    pass
    def display_data(self):
        pass

class managment:
    pass

S1=Student(10,"ALice",[87,95,89])
S1.display()
