"""



"""
from typing import List


def findRotateCount(nums: List[int]) -> int:
    left, right, length = 0, len(nums)-1, len(nums)-1

    while left <= right:
        if nums[left] <= nums[right]:
            return left
        mid = (left+right) // 2
        prev = (mid+length) % length
        next = (mid+1) % length
        if nums[prev] >= nums[mid] >= nums[next]:
            return mid
        if nums[left] <= nums[mid]:
            left = mid + 1
        else:
            right = mid - 1



