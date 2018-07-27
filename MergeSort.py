def mergeSort(data):
    print("Splitting ",data)
    if len(data)>1 :
        mid = len(data)//2
        left = data[:mid]
        right = data[mid:]
        mergeSort(left)
        mergeSort(right)
        i = 0 
        j = 0 
        k = 0 
        #First while to comapre the leftside and right side of divided list 
        while i<len(left) and  j<len(right) :
            if left[i] < right[j] :
                data[k] = left[i]
                i=i+1
            else:
                data[k] = right[j]
                j=j+1
            k=k+1
        #Another while loop to add remaining elements from left array to sorted lsit 
        while i<len(left):
            print("Left side still remain")
            data[k]=left[i]
            i=i+1
            k=k+1
    
        #Another while loop to add remaining elements from Right array to sorted lsit 
        while j<len(left) :
            print("Right side still remain")
            data[k]=right[j]
            j=j+1
            k=k+1
        


data = [54,26,93,17,77,31,44,55,20]
mergeSort(data)
print("Merged List",data)