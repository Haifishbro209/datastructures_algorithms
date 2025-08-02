from create_array import *
import time

def bubble_sort(arr):
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

arr = random_array(1000)
start = time.time()
bubble_sort(arr)
end = time.time()
print(f'Bubble sort: {end-start:.10f}')

start = time.time()
arr.sort()
end= time.time()
print(f'\n.sort(): {end-start:.10f}')