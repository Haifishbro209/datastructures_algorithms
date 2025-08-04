from create_array import *
from time import time
from sys import setrecursionlimit

setrecursionlimit(400000)




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
    arr[length -1] , arr[random_index] = arr[random_index] , arr[length-1]


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

if __name__ == '__main__':
    # Test array
    test_array = sorted_array(10000)


    start_time = time()
    quicksorted_array = quicksort(test_array)
    quicksort_time = time() - start_time

    if not is_sorted(quicksorted_array):
        print('QUICKSORT ERROR')

    start_time = time()
    sorted_arr = test_array.sort()
    sort_time = time() - start_time

    print(f"Quicksort time: {quicksort_time:.6f} seconds")
    print(f"Built-in sort time: {sort_time:.6f} seconds")
