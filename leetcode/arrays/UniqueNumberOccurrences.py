"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.



Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true


"""

from typing import List

def uniqueOccurrences(arr: List[int]) -> bool:
    orderMap = {}
    count = 0
    for ele in arr:
        if ele in orderMap:
            orderMap[ele] = 1 + orderMap.get(ele, 0)
    for value in orderMap.values():
        if count > 1:
            return False
        if value == 1:
            count += 1
    return count == 1

print(uniqueOccurrences([26,2,16,16,5,5,26,2,5,20,20,5,2,20,2,2,20,2,16,20,16,17,16,2,16,20,26,16]))