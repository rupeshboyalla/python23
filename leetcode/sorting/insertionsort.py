

def insertionsort(arr):
    n = len(arr)
    for i in range(0, n - 1):
        # Move arr[i + 1] to its correct position.
        j = i + 1
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j = j - 1

    return arr;
print(insertionsort( [-913743, 3241, 999999, 1243153, 0, 0, 999999999]))