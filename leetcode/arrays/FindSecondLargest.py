"""
Given an array of integers, our task is to write a program that efficiently finds the second-largest element
present in the array.

"""
from typing import List


def findSecondLargest(nums: List[int]):
    nums.sort()
    for i in range(reversed(len(nums), -1)):
        if nums[i] != nums[i-1]:
            return nums[i]




print(findSecondLargest([10, 5, 10]))
