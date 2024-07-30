"""

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.



Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0


"""

from typing import List

def numIdenticalPairs(nums:List[int]):
    count = 0
    for i in range(len(nums)):
      for j in range(i+1, len(nums)):
          if nums[i] == nums[j]:
              count += 1
    return count


# from leetcode
"""

Here what he is doing 
"""
def numIdenticalPairsLt(nums:List[int]):
    good_pairs = 0
    for j in range(len(nums)):
        for i in range(j):
            if nums[i] == nums[j]:
                good_pairs += 1
    return good_pairs
print(numIdenticalPairsLt([1,2,3,1,1,3]))
