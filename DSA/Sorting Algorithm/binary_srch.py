
        # Binary Search Algorithm //

def binarySearch(arr, low, high, key):
    while low <= high:
        mid = int((low + high) / 2)

        if (key == arr[mid]):
            return mid
        elif (key > arr[mid]):
            low = mid + 1
        else:
            high = mid - 1

    
    return -1


if __name__== '__main__':

    
    arr= [72, 107, 162, 166, 194, 214, 227, 249, 266, 275, 276, 312, 334, 392, 421, 441, 463, 509, 534, 555, 572, 584, 650, 732, 759, 807, 826, 947]
    
    # arr.append(989)
    # print(len(arr))

    key = 807
    found = binarySearch(arr, 0, len(arr) - 1, key)

    if (found == -1):
        print("Element Not Found!")
    else:
        print(f"Element Found at index: {found}")


