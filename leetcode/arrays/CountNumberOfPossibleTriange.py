"""
Given an unsorted array of positive integers,
find the number of triangles that can be formed with three different
array elements as three sides of triangles.
For a triangle to be possible from 3 values, the sum of any of the
two values (or sides) must be greater than the third value (or third side).


Input: arr= {4, 6, 3, 7}
Output: 3
Explanation: There are three triangles
possible {3, 4, 6}, {4, 6, 7} and {3, 6, 7}.
Note that {3, 4, 7} is not a possible triangle.

Input: arr= {10, 21, 22, 100, 101, 200, 300}.
Output: 6
Explanation: There can be 6 possible triangles:
{10, 21, 22}, {21, 100, 101}, {22, 100, 101},
{10, 100, 101}, {100, 101, 200} and {101, 200, 300}


Follow the given steps to solve the problem:

Sort the array and then take three variables l, r, and i, pointing to start, end-1, and array element starting from the end of the array.
Traverse the array from the end (n-1 to 1), and for each iteration keep the value of l = 0 and r = i-1


"""
from typing import List

def countAllPossible(arr:List[int]):
    length = len(arr)
    arr.sort()
    count = 0
    for i in range(length-1, 0, -1):
        left = 0
        right = i - 1
        while left < right:
            if arr[left] + arr[right] > arr[i]:
                count += right -1
                right -= 1
            else:
                left += 1
    print("No of possible solutions:", count)


if __name__ == '__main__':
    arr = [10, 21, 22, 100, 101, 200, 300]
    countAllPossible(arr)

