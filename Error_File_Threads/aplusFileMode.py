import os

os.chdir("D:\\Don't touch my file\\python_essentials\\Error_File_Threads")
with open("ProductData.txt","r+") as pd:
    for i in range(100):
        x=(input("Enter 0 for exit: "))
        if x=='0':
            break
        else:
            pname=(input("Enter product name: "))
            pprice=int(input("Enter price of the product: "))
            pqty=int(input("Enter product Quantity: "))
            ptotal=pprice*pqty
            pd.write(f"{pname}\t{pprice}\t{pqty}\t{ptotal}\n")
            pd.seek(0)
            print(pd.read())
