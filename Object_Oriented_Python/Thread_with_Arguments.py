#Passing arguments to a function by using threads
import threading
import time

def f1(a,b,c):
    print("This is Function")
    print(f"{a},{b},{c}")

t1=threading.Thread(target=f1,args=("Data","Tables","Columns"))
t1.start()
t1.join()

sq=[]
cb=[]

def squares(s,e,a,Name,Version):
    for i in range(s,e):
        print(a,time.ctime(),":",i*i)
        print(Name,Version,sep="\t")
        time.sleep(0.7)
        sq.append(i*i)

def cubes(s,e,b,Name,Version,Year):
    for i in range(s,e):
        print(b,time.strftime(" %H:%M:%S --"),":",i*i*i)
        print(Name,Version,Year,sep="\t")
        time.sleep(0.5)
        cb.append(i*i*i)

T1=threading.Thread(target=squares,args=(2,2,"squares"),kwargs={"Name":"Thread1","Version":1.25})
T2=threading.Thread(target=cubes,args=(2,4,"Cubes"),kwargs={"Name":"Thread2","Version":2.65,"Year":2027})

T1.start()
T2.start()
T1.join()
T2.join()

print(sq)
print(cb)

   

