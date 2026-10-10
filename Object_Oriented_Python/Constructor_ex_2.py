import random as r
class Employee:
    def __init__(self, name, department, designation, salary, city):
        self.name=name
        self.department=department
        self.designation=designation
        self.salary=salary
        self.city= city
        print("\n    ___Employee Details___")

    def display(self):
        code=r.randint(10000,99999)
        print(f"Employee ID: {code}")
        print(f"Employee Name: {self.name}")
        print(f"Employee Department: {self.department}")
        print(f"Designation of Employee: {self.designation}")
        print(f"Employee Salary: {self.salary} Rs/- monthly")
        self.annual_salary()
        print(f"Employee belongs to {self.city} city")
        
    def annual_salary(self):
        self.salary=self.salary*12
        print("Yearly salary: ",self.salary,"rupees per annum")

e1=Employee("Alice","mechanical department","team leader",105000,"mumbai")
e1.display()

e2=Employee("charly","civil department","developer",95000,"pune")
e2.display()
