
        # Binary Search Algorithm //

def binarySearch(arr, low, high, key):
    count=0
    while low <= high:
        mid = int((low + high) / 2)
        count+=1
        if (key == arr[mid]):
            return count
        elif (key > arr[mid]):
            low = mid + 1
        else:
            high = mid - 1

    
    return count


if __name__== '__main__':

    
    arr= [266,507,519,557,560,603,628,666,813,931]
    
    # arr.append(989)
    # print(len(arr))

    key = 266
    found = binarySearch(arr, 0, len(arr) - 1, key)

    print("No of iteration: ",found)

    # if (found == -1):
    #     print("Element Not Found!")
    # else:
    #     print(f"Element Found at index: {found}")


