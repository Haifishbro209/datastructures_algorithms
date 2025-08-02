from create_array import random_array


def sort(arr):
    length = len(arr)
    for i in range(length):
        a = arr[i]
        if i < length - 1:
            b = arr[i+1]
        else:
            break           
        if a > b:
            arr[i] = b
            arr[i+1] = a
    return arr

print(sort(random_array()))