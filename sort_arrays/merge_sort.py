array = [7,0,45,5,93,11,6]


def mergesort(arr):
    length = len(arr)
    if length < 2:
        return
    middle = int(length /2)

    leftarray = [0] * middle
    rightarray = [0] * (length - middle)

    for i in range(middle):
        leftarray[i] = arr[i]
    
    j = 0
    for i in range(middle +1, length -1):
        rightarray[j] = arr[i]
        j += 1

    mergesort(leftarray)
    mergesort(rightarray)    
    merge(leftarray,rightarray,arr)

def merge(left, right, array):
    left_size = len(left)
    right_size = len(array) - left_size

    i = 0
    r = 0
    l = 0
    
    while l < left_size and r < right_size:
        if left[l] < right[r]:
            array[i] = left[l]
            i+=1
            l +=1
        else:
            array[i] = right[r]
            i +=1
            r +=1
    

    while l < left_size :
        array[i]= left[l]

    while r < right_size:
        array[i]= right[r]
    
print(array)

mergesort(array)

print(array)

