
"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

https://leetcode.com/problems/contains-duplicate/


"""
from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    hashSet = set()
    for num in nums:
        if num in hashSet:
            return True
        hashSet.add(num)
    return False


print(containsDuplicate([1,2,3,1]))