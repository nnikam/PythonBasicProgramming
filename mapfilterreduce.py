'''
use of map,filter and reduce
'''
from functools import reduce

maxnum = lambda x,y: x if x>y else y 
data = [1,2,3,4,5,6,7,8,9]
print(list(map(lambda x:x*x,data)))
#print(squares_list(data))



print(list(filter(lambda x:x>5,data)))

print(reduce(lambda x,y : x if x>y else y  ,data))