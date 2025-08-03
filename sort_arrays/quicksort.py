from create_array import random_array
from random import randint


test_array = [4,5,2,7,9,89]


def quicksort(arr):
    length = len(arr)
    position = randint(0,length)
    split_point = arr[position]

    
    for i in range(position):
        if arr[i] > split_point:
            arr[position] = arr[i]
            arr.pop(i)
            position -= 1

    for i in range(position ,length):
        if arr[i] < split_point:
            arr[position] = arr[i]
            arr.pop(i)
            position += 1

    first_half = quicksort(arr[0:position])
    second_half = quicksort(arr[position +1:length])
    return arr
    

print(quicksort(test_array))

#arr = random_array(100)