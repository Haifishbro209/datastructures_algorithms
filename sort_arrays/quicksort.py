from create_array import *
from time import time
from sys import setrecursionlimit

setrecursionlimit(400000)

test_array = reversed_array(10000)



def quicksort(arr):
    first_part = None
    second_part = None

    if arr == []:
        return []
    length = len(arr)
    if length == 1:
        return arr
    
    random_index = randint(0,length-1)
    pivot = arr[random_index]
    swap =arr[length -1]
    arr[length -1] = pivot
    arr[random_index] = swap

    i = -1
    for j in range(length-1):
        if arr[j] < pivot:
            i += 1
            swap = arr[i]
            arr[i] = arr[j]
            arr[j] = swap
    
    swap = arr[i+1]
    arr[i+1] = pivot
    arr[length-1] = swap
    arr[0:i +1] = quicksort(arr[0:i+1])
    arr[i+2: length] = quicksort(arr[i + 2: length])

    return arr
start=time()
test_array = quicksort(test_array)
end=time()
print(end - start)
print(is_sorted(test_array))
