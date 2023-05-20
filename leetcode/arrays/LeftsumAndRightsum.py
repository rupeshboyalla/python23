
"""
Given, an array of size n. Find an element that divides the array into two sub-arrays with equal sums.

Examples:

Input: 1 4 2 5 0
Output: 2
Explanation: If 2 is the partition, subarrays are : [1, 4] and [5]

Input: 2 3 4 1 4 5
Output: 1
Explanation: If 1 is the partition, Subarrays are : [2, 3, 4] and [4, 5]
"""

from typing import List

def leftSumAndRightSum(nums:List[int]):
    length = len(nums)
    rightSumArr = [0] * length
    for i in reversed(range(length-1)):
        rightSumArr[i] = rightSumArr[i+1] + nums[i+1]
    leftSum = 0
    for i in range(length):
        if leftSum == rightSumArr[i]:
            return nums[i]
        leftSum += nums[i]

    return -1

print(leftSumAndRightSum([2, 3, 4, 1, 4, 5]))
