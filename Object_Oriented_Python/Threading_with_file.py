import threading
import os
import time

info=""

def read_write_file(file1,file2):
    os.chdir("D:\\Don't touch my file\\python_essentials\\Object_Oriented_Python")
    with open (file1,"r") as f1:
        info=f1.read()
        print(info)
        f1.close()

    os.chdir("D:\\Don't touch my file\\python_essentials\\Object_Oriented_Python")
    with open (file2, "w") as f2:
        f2.write(info)
        f2.close

t1=threading.Thread(target=read_write_file,args=("Input_file.txt","Output_file.txt"))

t1.start()
t1.join()
