"""
Given an integer array nums, find a
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""
from typing import List

def maxProduct(nums: List[int]) -> int:
    maxProd = nums[0]
    minProd = nums[0]
    result = 0
    for i in range(1, len(nums)):
        curMaxProd = max(maxProd*nums[i], minProd, nums[i])
        curMinProd = min(maxProd * nums[i], minProd, nums[i])
        result = max(result, curMaxProd)
        maxProd = curMaxProd
        minProd = curMinProd

    return result

print(maxProduct([-4,-3]))
