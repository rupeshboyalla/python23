"""

Given an array arr[] of integers, segregate even and odd numbers in the array.
Such that all the even numbers should be present first, and then the odd numbers.

Examples:

Input: arr[] = 1 9 5 3 2 6 7 11
Output: 2 6 5 3 1 9 7 11

Input: arr[] = 1 3 2 4 7 6 9 10
Output:  2 4 6 10 7 1 9 3


"""

def arrayEvenAndOdd(arr,  n):
    index = -1
    left = 0
    while left!=n:
        if arr[left]%2 == 0:
            index = index+1
            arr[index], arr[left] = arr[left], arr[index]

        left += 1
    return arr






arr = [1, 3, 2, 4, 7, 6, 9, 10]
n = len(arr)

# Function call
print(arrayEvenAndOdd(arr, n))