stock_list=[{"product_id":10001,"product_name":"Laptop","price":78499,"quantity":4},
            {"product_id":10002,"product_name":"CCTV Camera","price":4999,"quantity":12},
            {"product_id":10003,"product_name":"Wifi setup","price":9999,"quantity":7},
            {"product_id":10004,"product_name":"PC","price":15200,"quantity":2}]

def register_new_product():
    product_id=int(input("Enter product ID: "))
    product_name=input("Enter product name: ")
    product_price=int(input("Enter product price: "))
    product_quantity=int(input("Enter product quantity: "))
    stock_list.append({"product_id":product_id,"product_name":product_name,"price":product_price,"quantity":product_quantity})

def get_products_detail():
    print(stock_list)