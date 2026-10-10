class Personal:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

class Acedmics:
    def __init__(self,education,marks):
        self.education=education
        self.marks=marks

    def grade(self):
        tm=sum(self.marks)/len(self.marks)
        if 100>tm>=80:
            return "O"
        elif 80>tm>=65:
            return "A"
        elif 65>tm>=50:
            return "B"
        elif 50>tm>=40:
            return "C"
        else:
            return "F"

class Skill:
    def __init__(self,skillsets,salary):
        self.skillsets=skillsets
        self.salary=salary

class Employee:
    def __init__(self,name,emp_id,gender,education,marks,skillsets,salary,company_name):
        self.emp_id=emp_id
        self.company_name=company_name
        Personal.__init__(self,name,gender)
        Acedmics.__init__(self,education,marks)
        Skill.__init__(self,skillsets,salary)
        self.grade()

    def display(self):
        print(self.name,self.emp_id,self.gender,self.education,self.grade,self.skillsets,self.salary,self.company_name,sep="\n")

E1=Employee("X",71398,"male","M.Tech",[97,68,72],["CNN","GSC","AI"],120000,"Amazon DSA")
E1.display()
