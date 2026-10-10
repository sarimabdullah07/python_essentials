class School:
    #class variable
    school_motto="Strive for Exellence"

    #constructor(instance of a class)
    def __init__(self,p1,p2):
        #instance variable
        self.p1=p1
        self.p2=p2

    #instance of a class
    def display(self):
        print("Name of the student: ",self.p1)
        print("percentage of the student: ",self.p2,"%")
        print(self.school_motto)

    @classmethod
    def set_passing_marks(cls,marks):
        cls.marks=marks
        print("Minimum passing marks set to: ",marks)

#object(instances of a class)
s1=School("Abraham",92)
s1.display()

#class method calling
School.set_passing_marks(40)
