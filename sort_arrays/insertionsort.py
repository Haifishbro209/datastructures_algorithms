

def insertionsort(arr):
    length = len(arr)
    for i in range(1,length):
        temp = arr[i]
        j = i-1
        while temp < arr[j]:
            arr[j +1] = arr[j]
            if j > 1:
                break
            else:
                j -=1
        arr[j] = temp
    
    return arr


array = [3,8,9,6,1,7,2,4]

print(insertionsort(array))