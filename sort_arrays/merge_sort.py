
arr = [7,0,45,5,93,11,6]

def mergesort(arr):
    length = len(arr)
    if length > 2:
        mergesort(arr[0:int(length/2)])
        mergesort(arr[int(length /2)])
    else:
        sorted = merge([arr[0]],[arr[1]])
        return sorted
    
def merge(left,right):
    arr = []
    for i in left:
        for j in right:
            if i > j:
                arr.extend(j)
    

print(mergesort(arr))