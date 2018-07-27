import time 
import threading



def squares(data,timer):
    for n in data:
        time.sleep(timer)
        print("square="+str(n*n))
        
        
def cubes(data,timer):
    for n in data:
        time.sleep(timer)
        print("cube="+str(n*n*n))
        


data=[1,2,3,4,5,6]


start_time = time.time()

t1= threading.Thread(target=squares,args=(data,0.2))
t2= threading.Thread(target=cubes,args=(data,0.2))


print(dir(t1))

t1.start()
t2.start()

t1.join()
t2.join()





# squares(data)
# cubes(data)

print("Total Execution time is"+str(time.time()-start_time))









