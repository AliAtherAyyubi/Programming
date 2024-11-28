

#  insertion Sort 

def insertionSort(arr):

    for step in range(1,len(arr)):

        key=arr[step]
        j=step-1

        while key<arr[j] and j>=0:
            
            arr[j+1]=arr[j]
            j=j-1
        
        arr[j+1]=key


if __name__== "__main__":

    array=[4,33,2,12,34,2,1,3,-2]

    insertionSort(array)

    print(array)
