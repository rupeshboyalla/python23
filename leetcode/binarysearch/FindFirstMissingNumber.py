"""
Given a sorted array of n distinct integers where each integer is in the range from 0 to m-1 and m > n. Find the smallest number that is missing from the array.

Examples:

Input: {0, 1, 2, 6, 9}, n = 5, m = 10
Output: 3

Input: {4, 5, 10, 11}, n = 4, m = 12
Output: 0

Input: {0, 1, 2, 3}, n = 4, m = 5
Output: 4

Input: {0, 1, 2, 3, 4, 5, 6, 7, 10}, n = 9, m = 11
Output: 8


"""

# def findFirstMissing(array, start, end):
#
#     if start is None and end is None:
#         start, end = 0, len(array)-1
#
#     mid = start + (start - end)//2
#
#     if array[mid] == mid:
#         return findFirstMissing(array, mid+1, end)
#     return findFirstMissing(array, start, mid-1)
#
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 10]
# n = len(arr)
# print("Smallest missing element is",
#       findFirstMissing(arr, 0, n-1))

def findFirstMissing(array, start, end):
    if start > end:
        return end + 1

    if start != array[start]:
        return start

    mid = (start+end)//2

    # Left half has all elements
    # from 0 to mid
    if array[mid] == mid:
        return findFirstMissing(array,
                                mid + 1, end)

    return findFirstMissing(array,
                            start, mid)


# driver program to test above function
arr = [0, 1, 2, 3, 4, 5, 6, 7, 10]
n = len(arr)
print("Smallest missing element is",
      findFirstMissing(arr, 0, n - 1))