#Write a program to take any array with integers and move all the zeros to the end of the array. Preserve the order of the rest of the numbers.

#Input:
# Arrary A = [2, 3, 0, 8, 0, 10, 15, 0, 7]

#Output:
 #Arrary A = [2, 3, 8, 10, 15, 7, 0, 0, 0]

def pushZerosToEnd(arr):
    count = 0  # Count of non-zero elements

    # Traverse the array. If element
    # encountered is non-zero, then
    # replace the element at index
    # 'count' with this element
    n = len(arr)
    for i in range(n):
        if arr[i] != 0:
            # here count is incremented
            arr[count] = arr[i]
            count += 1

    # Now all non-zero elements have been
    # shifted to front and 'count' is set
    # as index of first 0. Make all
    # elements 0 from count to end.
    while count < n:
        arr[count] = 0
        count += 1


# Driver code
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
pushZerosToEnd(arr)
print("Array after pushing all zeros to end of array:")
print(arr)
