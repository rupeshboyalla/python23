"""

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.



Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


https://leetcode.com/problems/max-consecutive-ones-iii/



"""
from typing import List
def longestOnes(nums: List[int], k: int) -> int:
    left, count, right = 0, 0, 0
    length = len(nums)
    maxLength = 0
    while right < length:
        if nums[right] == 0:
            count += 1
        elif count == k:
            maxLength = max(maxLength, right-left)
            count = 0
            left += 1
        right += 1
    return maxLength
print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))


        