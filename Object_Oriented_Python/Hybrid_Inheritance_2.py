class Person:                      #Base Class
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Sports(Person):              #Single Inheritance
    def __init__(self,name,age,sport):
        super().__init__(name,age)
        self.sport=sport

        # print(self.name, self.age, self.sport, sep="    ")
class Acedmics(Person):            
    def __init__(self,name,age,education,result):
        super().__init__(name,age)
        self.education=education
        self.result=result

class Skill(Person):
    def __init__(self,name,age,skill):
        super().__init__(name,age)
        self.skill=skill

class Employee(Acedmics,Skill):
    def __init__(self,name, age, education, result, skill, designation):
        Acedmics.__init__(self,name,age,education,result)
        Skill.__init__(self,name,age,skill)
        # Person.__int__(self, name, age)
        # self.education = education
        # self.result = result
        # self.skill = skill
        self.designation=designation

    def display(self):
        print(self.name)
        print(self.age)
        print(self.education)
        print(self.result)
        print(self.skill)
        print(self.designation)

E=Employee("Alice",23,"M.Tech","O grade","Problem Solving","HR")
E.display()

# S=Sports("Aabid",16,"UFC")
