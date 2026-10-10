def amount_discount(price,qty):
    amount=price*qty
    if amount>=10000:
        discount=0.1
    elif amount>=5000:
        discount=0.05
    else:
        discount=0
    return amount-discount*amount

a=amount_discount(2000,10)
print(a)


def sum(a,b):
    c=a+b
    print(c)
sum(2,3)
