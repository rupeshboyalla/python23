"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from typing import List

# 2 ways we can do this problem which is using hashtable or binary search

def topKFrequent(nums: List[int], k: int) -> List[int]:
    lookupTable = {}
    for num in nums:
        lookupTable[num] = 1+lookupTable.get(num, 0)
    result = []
    for key, value in lookupTable.items():
        if value >= k:
            result.append(key)
    return result
print(topKFrequent([1,1,1,2,2,3], 2))
