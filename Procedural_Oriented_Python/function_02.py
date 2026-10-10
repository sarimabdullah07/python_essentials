def dictionary_maker(product,price):
    Dict=dict()
    if len(product)!=len(price):
        print("Enter proper data")
    else:
        for i in range(len(price)):
            Dict[product[i]]=price[i]
    return Dict

a=dictionary_maker(["SSD","intel core i5","Graphic Card"],[8500,20000,45000])
print(a)

def avg(element):
    a=sum(element)
    b=element.count
    c=a/b
    print(c)

avg([20,30,40])
