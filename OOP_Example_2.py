import random as r
class Employee:
    def __init__(self, name, department, designation, salary, city):
        self.name=name
        self.department=department
        self.designation=designation
        self.salary=salary
        self.city= city
        print("___Employee Details___")

    def display(self):
        code=r.randint(10000,99999)
        print(f"Employee ID: {code}")
        print(f"Employee Name: {self.name}")
        print(f"Employee Department: {self.department}")
        print(f"Designation of Employee: {self.designation}")
        print(f"Employee Salary: {self.salary} Rs/- monthly")
        print("Employee yearly Salary: ",self.salary*12, "rupee per annum")
        print(f"Employee belongs to {self.city} city")
        

e=Employee("Alice","mechanical department","team leader",105000,"mumbai")
e.display()