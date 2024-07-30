"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


"""
from typing import List


def searchRange(nums: List[int], target: int, ) -> List[int]:
    return [search(nums, target, True), search(nums, target, False)]


def search(nums:List[int], target:int, isFirstOccurrence: bool) -> int:
    left, right = 0, len(nums)-1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            if isFirstOccurrence:
                right = mid - 1
            else:
                left = mid + 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return result
print(searchRange( [5,7,7,8,8,10], 8))