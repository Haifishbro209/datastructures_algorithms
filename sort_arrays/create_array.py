from random import randint

def random_array(length = 100):
    arr = []
    for i in range(length):
        arr.append(randint(-10000, 10000))

    return arr


def sorted_array(length = 100):
    arr=[]
    for i in range(length):
        arr.append(i - int(0.5 * length))
    return arr


def reversed_array(length = 100):
    arr=[]
    for i in range(length):
        arr.append(-i + int(0.5 * length))
    return arr

def is_sorted(arr):
    for i in range(1,len(arr) -1):
        if arr[i] < arr[i -1]:
            return False
    return True

if __name__ == '__main__':
    pass