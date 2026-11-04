import os
os.chdir("D:\\Don't touch my file\\python_essentials\\Error_File_Threads")

class EmpSal:
    def __init__(self,source,dest):
        self.source=source
        self.dest=dest

    def readata(self):
        with open(self.source,"r") as fr, open(self.dest, "w") as fw:
            a=fr.readlines()
            for i in a:
                b=i.split()
                fw.write(f"{b[0] } salary {b[-1]}\n")
            fw.close()
        fr.close()

f1=EmpSal("EmployeeData.txt","Employee_Salary")
f1.readata()






