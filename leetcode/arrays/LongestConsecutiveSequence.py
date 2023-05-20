
"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


https://leetcode.com/problems/longest-consecutive-sequence/

"""

from typing import List

def longestConsecutive(nums: List[int]) -> int:
    nums = sorted(nums)
    result = 0
    currentLongest = 1
    for right in range(1, len(nums)):
        if nums[right] == nums[right-1]:
            continue
        elif nums[right] == nums[right-1] + 1:
            currentLongest += 1
        else:
            result, currentLongest = max(result, currentLongest), 1
    return max(result, currentLongest)
print(longestConsecutive([100,4,200,1,3,2]))