class Employee:
    def __init__(self,id,name,gender):
        self.id=id
        self.name=name
        self.gender=gender
    def display(self):
        print("\nEmployee ID: ",self.id,"\nName: ",self.name,"Gender: ",self.gender)

class FrontEnd(Employee):
    def __init__(self,id,name,gender,software):
        super().__init__(id,name,gender)
        self.software=software

    def display_F(self):
        super().display()
        print("Software Name: ",self.software)

class DataBase(Employee):
    def __init__(self,id,name,gender,work):
        super().__init__(id,name,gender)
        self.work=work

    def display_D(self):
        super().display()
        print("Designation: ",self.work)

class BackEnd(Employee):
    def __init__(self,id,name,gender,language):
        super().__init__(id,name,gender)
        self.language=language
    def display_BK(self):
        super().display()
        print("Langage: ",self.language)

F1=FrontEnd(1001,"Alice","Male","JavaScript\n")
D=DataBase(1002,"Bob","Male","Security\n")
B=BackEnd(1003,"Maryam","Female","Java\n")

F1.display_F()
D.display_D()
B.display_BK()
