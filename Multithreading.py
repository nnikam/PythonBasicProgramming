import threading
import time 


def cube(num):
    for item in num:
        time.sleep(0.2)
        print("Cube=>"+str((item*item*item)))



def square(num):
    for item in num:
        time.sleep(0.2)
        print("Square=>"+str((item*item)))
        


data=[5,4,3,2,1]


t1=threading.Thread(target=square,args=(data,))
t2=threading.Thread(target=cube,args=(data,))

start_time = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

print("The total time needed to complete execution is "+str(time.time()-start_time))





            




            

