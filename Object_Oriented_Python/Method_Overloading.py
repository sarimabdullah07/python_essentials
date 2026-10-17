class Calculator:
    def add(self, a, b, c=0):
        print(a + b + c)

obj = Calculator()
obj.add(2, 3)
obj.add(2, 3, 4)