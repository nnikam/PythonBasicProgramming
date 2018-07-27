try:
    x= 10/2
    
except ZeroDivisionError  as e:
    print(e)
else:
    print("Inside Else block")
finally:
    print("Done finally")
    
