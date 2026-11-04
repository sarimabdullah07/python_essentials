import csv

# data_to_write=[{'emp_id': '1010', 'emp_name': 'Alice ', 'emp_gender': 'Male', 'emp_city': 'Mumbai', 'emp_salary': '95000'},
# {'emp_id': '1011', 'emp_name': 'Bella', 'emp_gender': 'Female', 'emp_city': 'Pune', 'emp_salary': '76500'},
# {'emp_id': '1012', 'emp_name': 'Charlie', 'emp_gender': 'Male', 'emp_city': 'Nashik', 'emp_salary': '85300'},
# {'emp_id': '1013', 'emp_name': 'David', 'emp_gender': 'Male', 'emp_city': 'Nagpur', 'emp_salary': '120000'},
# {'emp_id': '1014', 'emp_name': 'Eve', 'emp_gender': 'Female', 'emp_city': 'Mumbai', 'emp_salary': '62300'},
# {'emp_id': '1015', 'emp_name': 'Frankie', 'emp_gender': 'Male', 'emp_city': 'Aurangabaad', 'emp_salary': '89650'}]

# with open("NewData_02.csv","w") as cf:
#     fields=["emp_id","emp_name","emp_gender","emp_city","emp_salary"]
#     csvwriter=csv.DictWriter(cf,fieldnames=fields)
#     csvwriter.writeheader()
#     csvwriter.writerows(data_to_write)
#     cf.close()
with open("EmployeeData_02_csv.csv","r") as cf:    
    csvreader=csv.DictReader(cf)
    total=0
    for i in csvreader:
        if i["emp_gender"]=="Male":
            i["emp_salary"]=int(i["emp_salary"])+0.1*int(i["emp_salary"])
            print(f"{i["emp_id"]} {i["emp_gender"]} --> {i["emp_salary"]}")