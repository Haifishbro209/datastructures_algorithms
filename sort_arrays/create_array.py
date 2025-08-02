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

