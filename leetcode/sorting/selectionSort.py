"""

How to sort an array using the traditional sorting method is selection sort


"""
from typing import List
def sort(nums:List[int]):
    for i in range(len(nums)):
        min_index = i
        min_value = nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] < min_value:
                min_value = nums[j]
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

print(sort([5,7,4,2,1]))
