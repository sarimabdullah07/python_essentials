import os
os.chdir("D:\\")
try:
    with open("D:\\Don't touch my file\\python_essentials\\Error, File, Threads\\file_02.txt","w") as wf:
        wf.write("This file is actually not created first, write function creates file if not found in the given address\n And it rewrite(Delete prevoius data) for every writing.")
        wf.close
except FileNotFoundError:
    print("Not able to write.. may be space or restricted setting")