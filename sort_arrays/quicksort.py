from create_array import random_array
from random import randint


test_array = [4,5,2,7,9,89]


def quicksort(arr):
    length = len(arr)
    if length == 0: return arr
    if length == 1:
        position = 0
    else:
        position = randint(0,length -1)

    split_point = arr[position]


    
    for i in range(position -1):
        if arr[i] > split_point:
            arr[position] = arr[i]
            arr.pop(i)
            position -= 1

    for i in range(position ,length -1):
        if arr[i] < split_point:
            arr.insert(position,arr[i])
            arr.pop(i)
            position += 1

    first_half = quicksort(arr[0:position])
    second_half = quicksort(arr[position +1:length])
    print(f'arr == {arr}')
    print(f'first_half == {first_half}')
    print(f'second_half == {second_half}')
    return arr
    

print(quicksort(test_array))

#arr = random_array(100)