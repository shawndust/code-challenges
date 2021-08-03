def rotateLeft(d, arr):
    for i in range(d):
        arr.append(arr[0])
        arr.pop(0)
    return arr
