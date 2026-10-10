#Multiple Inheritance

class Personal:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

class Acadmics:
    def __init__(self,education,marks):
        self.education=education
        self.marks=marks
    def grade(self):
        tm=round(sum(self.marks)/len(self.marks),2)
        if 100>tm>=90:
            return "A"
        elif 90>tm>=80:
            return "B"
        elif 80>tm>=70:
            return "C"
        elif 70>tm>=60:
            return "D"
        else:
            return "Not Statisfy"

class Skills:
    def __init__(self,skillset):
        self.skillset=skillset
    def salary(self):
        if self.grade() == "A":
            return 80000
        elif self.grade() == "B":
            return 70000
        elif self.grade() == "C":
            return 60000
        elif self.grade() == "D":
            return 50000
        else:
            return 40000
    def gross_salary(self):
        annual=self.salary()*12
        if 100000>self.salary()>=80000:
        #     annual=annual+15000
        # # elif 80000>self.salary>=60000:
        # #     annual=annual+10000
        # # else:
        # #     annual=annual+5000
        return annual
    

class Employee(Personal,Acadmics,Skills):
    def __init__(self,name,gender,department,education,marks,skillset):
        Personal.__init__(self, name, gender)
        Acadmics.__init__(self, education, marks)
        Skills.__init__(self, skillset)
        self.department=department

    def display(self):
        print("Name: ",self.name)
        print("Gender: ",self.gender)
        print("Department: ",self.department)
        print("Highest Education: ",self.education)
        print("Grade: ",self.grade())
        print("Skills: ",self.skillset)
        print("Salary: ",self.salary())
        print("Gross_Salary: ",self.gross_salary())

E1=Employee("Alice","Male","Artificial Intelligence","M.Tech",[90,80,79],["Advance Python","Random Forest expert","Matlab","GSC analyst"])
E1.display()