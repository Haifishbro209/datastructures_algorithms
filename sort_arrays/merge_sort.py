from create_array import *
from time import time

array = random_array(10000)
arr = array

def mergesort(arr):
    length = len(arr)
    if length < 2:
        return
    middle = int(length / 2)

    leftarray = [0] * middle
    rightarray = [0] * (length - middle)

    for i in range(middle):
        leftarray[i] = arr[i]

    j = 0
    for i in range(middle, length):
        rightarray[j] = arr[i]
        j += 1

    mergesort(leftarray)
    mergesort(rightarray)
    merge(leftarray, rightarray, arr)


def merge(left, right, array):
    left_size = len(left)
    right_size = len(right)

    i = 0
    r = 0
    l = 0

    while l < left_size and r < right_size:
        if left[l] < right[r]:
            array[i] = left[l]
            i += 1
            l += 1
        else:
            array[i] = right[r]
            i += 1
            r += 1

    while l < left_size:
        array[i] = left[l]
        i += 1
        l += 1

    while r < right_size:
        array[i] = right[r]
        i += 1
        r += 1

start = time()
mergesort(array)
end = time()
print(f'time = {end -start:.10f}')
print(is_sorted(array))


start = time()
arr.sort()
end = time()
print(f'time .sort() = {end -start:.10f}')
print(is_sorted(arr))
