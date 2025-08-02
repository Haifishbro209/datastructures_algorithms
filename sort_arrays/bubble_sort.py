from create_array import *


def sort(arr):
    length = len(arr)
    for j in range(length):
        for i in range(length - j):
            a = arr[i]
            if i < length - 1:
                b = arr[i+1]
            else:
                break           
            if a > b:
                arr[i] = b
                arr[i+1] = a
    return arr

arr = random_array(100000)
sorted = sort(arr)
print(f'{sorted} \n \n \n {is_sorted(sorted)}')