import os
import time
import threading
print("File Handling and Threads")
lines=""
os.chdir("D:\\Don't touch my file\\python_essentials\\Object_Oriented_Python")
with open("file_1.txt","r") as fr:
    lines=fr.readlines()
    with open("Destination_file.txt","w") as df:
        for i in lines:
            df.write(f"{time.strftime("%M:%S  ")} {i}")
        df.close()
    fr.close()

