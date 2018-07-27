import time 
import multiprocessing



def squares(data,timer=0.2):
    for n in data:
        time.sleep(timer)
        print("square="+str(n*n))
        
        
def cubes(data,timer=0.2):
    for n in data:
        time.sleep(timer)
        print("cube="+str(n*n*n))
        


data=[1,2,3,4,5,6]


start_time = time.time()

p1 = multiprocessing.Process(target=squares,args=(data,))
p2 = multiprocessing.Process(target=cubes,args=(data,))


p1.start()
p2.start()


p1.join()
p2.join()


print("Total Execution time is"+str(time.time()-start_time))









