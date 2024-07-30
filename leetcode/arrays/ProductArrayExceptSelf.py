"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


"""

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    length = len(nums)
    leftProd = [1] * length
    rightProd = [1]* length
    result =[1] * length
    for i in range(1, length):
        leftProd[i] = leftProd[i-1] * nums[i-1]
    for i in reversed(range(length - 1)):
        rightProd[i] = rightProd[i+1]*nums[i+1]
    for i in range(length):
        result[i] = leftProd[i] * rightProd[i]
    return result



print(productExceptSelf([1,2,3,4]))
