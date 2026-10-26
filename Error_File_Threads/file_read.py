import os

os.chdir("D:\\")
print(os.getcwd())
'''
with open("D:\\Don't touch my file\\python_essentials\\Error, File, Threads\\file_01.txt","r") as rf:
    print(rf.read())
    rf.close
'''
try:
    with open("D:\\Don't touch my file\\python_essentials\\Error, File, Threads\\file_01.txt","r") as rf:
        print(rf.read())
        rf.close
except FileNotFoundError:
    print("There is no file with given name or may be not found")
    

