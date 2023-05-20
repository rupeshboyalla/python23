"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


"""
from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    orderOfEle = {}
    for i in range(0, len(nums)):
        if nums[i] in orderOfEle:
            if i-orderOfEle.get(nums[i]) <= k:
                return True
            else:
                orderOfEle[nums[i]] = i
        else:
            orderOfEle[nums[i]] = i
    return False
# leetcode solution

def containsNearbyDuplicateLC(nums: List[int], k: int) -> bool:
    orderMap = {}
    for idx, ele in enumerate(nums):
        if ele in orderMap and idx - orderMap[ele] <= k:
            return True
        else:
            orderMap[ele] = idx
    return False




print(containsNearbyDuplicate([1,2,3,1], 3))