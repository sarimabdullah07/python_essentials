import time
import threading

def Display():
    list=[3,4,5,1,8,4,7,6,9,6,0]
    for i in list:
        print("Display ",i)
        time.sleep(2)

def Sum():
    list=[3,4,5,1,8,4,7,6,9,6,0]
    s=0
    for i in list:
        s+=i
        print("Sum= ",s)
        time.sleep(2)

def StringF():
    string="Hello Guys"
    s=[]
    for i in string:
        s.append(i)
        print("string ",s)
        time.sleep(2)

t1=threading.Thread(target=Display)
t2=threading.Thread(target=Sum)
t3=threading.Thread(target=StringF)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


'''
Multiple processes (functions) by time slice..
or run for a particular time and then switches to next process.

KNOWN AS MULTI THREADINGS
'''