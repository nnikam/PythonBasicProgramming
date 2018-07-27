def factorial(n):
    if n==1:
        return n 
    else:
        return n*factorial(n-1)
        
 
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
        

n=10
print(factorial(n))


for i in range(n):
    print(fibonacci(i))