import os
import csv

# with open("CSV_File.csv","r") as cf:
#     Ojt=csv.reader(cf)
#     total=0
#     for i in Ojt:
#         print(i)
#         total+=int(i[-1])
#     cf.close()
# print("Total Bill Amount = ",total," only..!")

with open("CSV_File.csv","a",newline="") as cf:
    Ojt = csv.writer(cf)
    for i in range(3):
        print(i)
        pid = int(input("Enter product ID: "))
        pname = input("Enter product name: ")
        pprice = int(input("Enter product price: "))
        pqty = int(input("Enter quantity: "))
        pamount = pqty * pprice
        total = [pid,pname,pprice,pqty,pamount]
        print(total)
        Ojt.writerow(total)
    cf.close()

