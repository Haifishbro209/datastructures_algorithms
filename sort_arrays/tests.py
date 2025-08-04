import sys
from time import time
from create_array import *


print("Aktuelles Limit:", sys.getrecursionlimit())

arr = random_array(10000)

length = len(arr)
random_index = randint(0,length-1)

pivot = arr[random_index]


def swap_time():
    start = time()
    swap =arr[length -1]
    arr[length -1] = pivot
    arr[random_index] = swap
    end = time()
    time_passed = end -start
    print(f'swap variable time {time_passed:.20f}')
    return time_passed


def one_line_time():
    start = time()
    arr[length -1] , arr[random_index] = arr[random_index] , arr[length-1]
    end = time()
    time_passed = end -start
    print(f'one line swap time {time_passed:.20f}')
    return time_passed

swap_was_faster = 0
one_line_was_faster = 0
equal = 0
dif = []
for i in range(10000):
    if i % 2 == 0:
        swap = swap_time()
        one_line = one_line_time()
    else:
        one_line = one_line_time()  
        swap = swap_time()
    
    if swap > one_line:
        one_line_was_faster +=1

    if one_line > swap:
        swap_was_faster +=1
    
    if one_line == swap:
        equal +=1

    dif.append(swap - one_line)

for diference in dif:
    

print(f'swap faster {swap_was_faster}')
print(f' one line faster {one_line} ')
print(f'equal {equal}')
