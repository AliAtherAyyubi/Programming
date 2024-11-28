
# Selection Sort algorithm


def SelectSort(array,size):
    
    for i in range(size):
        min=i
        for j in range(i+1,size):
            if array[min]>array[j]:
                min=j

        temp= array[i]
        array[i]=array[min]
        array[min]=temp


data= [34,22,4,-2,0,2,55,6]
size= len(data)

SelectSort(data,size)

print("Sorted Array")
print(data)
            
