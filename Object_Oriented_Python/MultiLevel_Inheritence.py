class Product:
    def __init__(self,pid):
        self.pid=pid

class Category(Product):
    def __init__(self,pid,category,name,price):
        super().__init__(pid)
        self.category=category
        self.name=name
        self.price=price

class Order(Category):
    def __init__(self,pid,category,name,price,quantity,pay_method):
        super().__init__(pid,category,name,price)
        self.quantity=quantity
        self.pay_method=pay_method

    def amount(self):
        # print("  ___Order Details___")
        print(self.pid,self.category,self.name,self.price,self.quantity,self.pay_method,sep="\t")
        return self.quantity*self.price

o1=Order(1001,"Electronics","Keyboard",2700,3,"UPI")
o2=Order(1002,"Home Appliances","Refrigrator",32900,2,"COD")
o3=Order(1003,"Electronics","Camera",8210,1,"Credit_Card")
o4=Order(1004,"Statonary","Book",250,6,"COD")
list=[o1,o2,o3,o4]
t=0
for i in list:
    t+=i.amount()
print("Total Bill Amount: ",t)