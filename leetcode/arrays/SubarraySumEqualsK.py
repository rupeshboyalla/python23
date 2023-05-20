"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

 https://leetcode.com/problems/subarray-sum-equals-k/description/



"""


from typing import List
def subarraySum(nums: List[int], k: int) -> int:
    lookupTable = {}
    lookupTable[0] = 1
    sum = 0
    count = 0
    for num in nums:
        sum += num
        if sum-k in lookupTable:
            count += lookupTable.get(sum-k)
        lookupTable[sum] = 1 + lookupTable.get(sum, 0)
    return count

print(subarraySum([1,1,1], 2))
