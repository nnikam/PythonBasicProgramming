mylist = [5,7,0,2,6]

mylist.sort(reverse=False)
print(mylist)




a=['name','surname','education','salary']
b=['John','root','Bachelor','60000']


person= {key:value for key,value in zip(a,b) if key!='education'}
print(person)

'''
Python program to find length of given number
'''
n = int(input("Please enter number"))

count=0 

while(n>0):
    count+=1
    n=n//10

# print("count=>",count)

'''
pytho Program to reverse the number
'''
n = int(input("Please enter number"))
reverse_num = 0
while(n>0):
    reminder = n%10   #this will give reminder 
    reverse_num = reverse_num*10+reminder
    n=n//10 #This will give the remaining number 
    
print(reverse_num)
    
    




