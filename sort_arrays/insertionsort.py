from time import time
from create_array import *

def insertionsort(arr):
    length = len(arr)
    for i in range(1,length):
        temp = arr[i]
        j = i-1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j +1] = temp
    
    return arr


array = random_array(10000)

start = time()
new_arr = insertionsort(array)
end = time()

print(f'insertionsort : {end -start:.10f}')

print(is_sorted(new_arr))

start = time()
new_arr = array.sort()
end = time()

print(f'.sort() : {end - start:.20f}')