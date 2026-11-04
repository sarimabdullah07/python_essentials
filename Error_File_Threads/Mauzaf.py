import csv
fields=["emp_id","emp_name","emp_gender","emp_dept","emp_role","emp_age","emp_salary"]
def create_csv():
    with open("Mauzaf.csv","w",newline="") as file:
        csvWriter=csv.DictWriter(file,fieldnames=fields)
        csvWriter.writeheader()
        file.close()

def append_records():
    with open("Mauzaf.csv","a",newline="") as file:
        csvWriter=csv.DictWriter(file,fieldnames=fields)

        emp=dict()

        emp_id=int(input("Enter ID: "))
        emp.update({"emp_id":emp_id})

        emp_name=(input("Enter Name: "))
        emp.update({"emp_name":emp_name})

        emp_gender=(input("Enter Gender: "))
        if emp_gender in ("Male","male","Female","female","MALE","FEMALE"):
            emp.update({"emp_gender":emp_gender})
        else:
            print("Invalid Gender")

        emp_dept=(input("Enter Departrment: "))
        if emp_dept in ("Sales","Logistic","Marketing","IT","Developer"):
            emp.update({"emp_dept":emp_dept})
        else:
            print("Invalid Department!")

        emp_role=(input("Enter Role: "))
        if emp_role in ("Software engineer","full stack devloper","Data Analyst","sales manager"):
            emp.update({"emp_role":emp_role})
        else:
            print("Invalid Role")

        emp_age=int(input("Enter Age: "))
        if 60>emp_age>20:
            emp.update({"emp_age":emp_age})
        else:
            print("Invalid Age")

        emp_salary=int(input("Enter Salary: "))
        if 200000>emp_salary>10000:
            emp.update({"emp_salary":emp_salary})
        else:
            print("Invalid Salary")

        print(emp)
        csvWriter.writerow(emp)
        file.close()

create_csv()
append_records()