	
import random
#generator Example1
def square_nums(nums):
    for item in nums:
        yield(item*item)
        

nums = square_nums([1,2,3,4,5,6,7,8,9,10])

for num in nums:
    print(num)

	


#Generator Example2
names = ['nitin','rahul','ram','RK','John','Joe']
age=[40,30,50,78,54,45]


def generatePersons(pnumbers):
    for i in range(pnumbers):
        persons={'id':i,
                 'name':random.choice(names),
                 'age':random.choice(age)
        }
        yield persons



p  = generatePersons(10)
print(p)
for item in p:
    print(item)