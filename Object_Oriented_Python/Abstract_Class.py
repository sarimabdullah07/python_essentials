from abc import ABC,abstractmethod
class Data(ABC):
    def __init__(self,a):
        print("This is constructor in abstract base class")
        self.a=a**2

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def show(self):
        pass

    def mymethod(self):
        print("Concrete method")

class NewData(Data):
    def __init__(self, a,b):
        super().__init__(a)
        self.b=b**3

    def show(self):
        print("This is the implementaion of show method")
        print(self.a)
        print(self.b)

    def display(self):
        print("This is the implementaion of display method")
        return super().display()

N1=NewData(5,9)
N1.display()
N1.show()
N1.mymethod()