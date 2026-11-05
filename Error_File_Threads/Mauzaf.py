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
        emp_name=(input("Enter Name: "))
        emp.update({"emp_id":emp_id},{"emp_name":emp_name})

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

def display_records():
    with open("Mauzaf.csv","r") as infile:
        csvReader=csv.DictReader(infile)
        records=list(csvReader)

        if len(records)==0:
            print("No Records available...")
        else:
            return records

def checkEmpId(id):
    found=False
    allrecords=display_records()
    for i in allrecords:
        if id==int(i["emp_id"]):
            print(i)
            found=True
    if found==False:
        print("No records found")

def male_salary(g,s):
    records=display_records()
    for i in records:
        if i["emp_gender"]==g and float(i["emp_salary"])>=30000:
            print(i)

def display_ascending():
    records=display_records()
    temp=dict()
    for i in range(len(records)):
        for j in range(i+1,len(records)):
            if records[i]["emp_name"]>records[j]["emp_name"]:
                temp=records[i]
                records[i]=records[j]
                records[j]=temp
    for i in records:
        print(i)

def increments():
    rec=display_records()
    for i in rec:
        if i["emp_dept"]=="Developer":
            i["emp_salary"]=84500
    for i in rec:
        print(i)

# create_csv()
# append_records()
# print(display_records())
# checkEmpId(103)
# male_salary("Male",30000)
# display_ascending()
increments()


