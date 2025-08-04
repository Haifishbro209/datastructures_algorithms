from create_array import random_array
from random import randint


test_array = [4,5,2,7,9,89,12,6]


def quicksort(arr):
    length = len(arr)
    pivot = arr[length-1]
    swap = 0
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

    if length > 1:
        first_part = quicksort(arr[0:i])
        second_part = quicksort(arr[i + 2: length])
    
    return first_part + [pivot] + second_part

print(quicksort(test_array))

