class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

    def display(self):
        print(f"Name of Student: {self.name}")
        print(f"Roll no: {self.roll_no}")
        print(f"Total marks: {sum(self.marks)}")
        print(f"Percentage: {sum(self.marks)/len(self.marks)}")

S1=Student(10,"ALice",[82,94,89])
S1.display()

s2=Student(24,"David",[92,79,62])
s2.display()