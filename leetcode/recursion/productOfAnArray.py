def productOfArray(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[len(arr)-1] * productOfArray(arr[:len(arr)-1])