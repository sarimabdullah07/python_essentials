class School:
    #class variable
    class_variable="You are very genius boy"

    #constructor(instance of a class)
    def __init__(self,p1,p2):
        #instance variable
        self.p1=p1
        self.p2=p2

    #instance of a class
    def display(self):
        print("Name of the student: ",self.p1)
        print("percentage of the student: ",self.p2,"%")
        print(self.class_variable)

    @classmethod
    def class_method(cls,iq):
        cls.iq=iq
        print("Your IQ level is",iq)

#object(instances of a class)
s1=School("Abraham",92)
s1.display()

#class method calling
School.class_method(164)
