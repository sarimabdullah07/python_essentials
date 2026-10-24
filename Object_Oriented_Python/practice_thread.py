import threading
import time

def square(start,end,Location,Pincode):
    for i in range(start,end):
        print("\n Square of",i,"is",i*i)
        time.sleep(0.5)
        print(Location, Pincode)
        print("\n Actual time: ",time.ctime())

def cube(start,end):
    for i in range(start,end):
        print("\n Cube of",i,"is",i*i*i)
        time.sleep(0.5)
        print("\n Actual time: ",time.strftime(" %H,%M,%S "))

t1=threading.Thread(target=square,args=(1,5),kwargs={"Location":"Mumbai","Pincode":123456})
t2=threading.Thread(target=cube,args=(1,5))

t1.start()
t2.start()

t1.join()
t2.join()