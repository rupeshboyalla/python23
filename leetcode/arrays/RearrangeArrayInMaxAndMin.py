"""
Rearrange an array in maximum minimum form using Two Pointer Technique

Given a sorted array of positive integers, rearrange the array alternately i.e first element should be a maximum value, at second position minimum value, at third position second max, at fourth position second min, and so on.

Examples:

Input: arr[] = {1, 2, 3, 4, 5, 6, 7}
Output: arr[] = {7, 1, 6, 2, 5, 3, 4}

Input: arr[] = {1, 2, 3, 4, 5, 6}
Output: arr[] = {6, 1, 5, 2, 4, 3}

"""

from typing import List


def rearrange(nums: List[int]):
    left, right = 0, len(nums) - 1
    result = [0] * len(nums)
    flag = True
    for i in range(len(nums)):
        if flag:
            result[i] = nums[right]
            right -= 1
        else:
            result[i] = nums[left]
            left += 1
        flag = bool(1 - flag)
    return result


print(rearrange([1, 2, 3, 4, 5, 6]))
