list_of_customer=[{"customer_id":1001,"customer_name":"Alice","customer_email":"alice123@gmail.com"},
                  {"customer_id":1002,"customer_name":"Bob","customer_email":"bob7024@gmail.com"},
                  {"customer_id":1003,"customer_name":"Charli","customer_email":"charli@gmail.co"}]

def register_new_customer():
    customer_id=int(input("Enter customer ID: "))
    customer_name=input("Enter customer Name: ")
    customer_email=input("Enter customer Email: ")
    list_of_customer.append({"customer_id":customer_id,"customer_name":customer_name,"customer_email":customer_email})
    print("__Customer registration successfully completed__")

def get_customer_detail():
    print(list_of_customer)
