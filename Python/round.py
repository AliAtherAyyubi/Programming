

def swap(n1,n2):
    temp=n2
    n2=n1
    n1=temp
    return n1,n2

arr= [8,10,14,14,18]

size=len(arr)
count=0
for i in range(size):
    idx=i
    for j in range(i+1,size):
        count+=1
        if arr[idx]>arr[j]:
            idx=j
    swap(arr[i],arr[j])

print(count+5)

# n1=6
# n2=7
# swap(n1,n2)

# print(swap(n1,n2))