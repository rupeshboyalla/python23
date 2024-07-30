"""

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.



"""
from typing import List


# def longestCommonPrefix(strs: List[str]) -> str:
#     minValue = len(min(strs, key= len))
#     low, high = 0, minValue-1
#     while low < high:
#         mid = (low+high)//2
#         if isCommonPrefix(strs, mid):
#             low = mid +1
#         else:
#             high = mid -1
#     return strs[0][:low-1]
#
#
# def isCommonPrefix(strs, mid):
#     minStr = strs[0][:mid]
#     for str in strs:
#         if str[:mid] != minStr:
#             return False.
#     return True

#method 2995
def longestCommonPrefix2(strs: List[str]) -> str:
    minLen = len(min(strs, key=len))
    minStr = strs[0][:minLen]
    for i in range(1, len(strs)):
        while strs[i].find(minStr) != 0:
            minStr = minStr[:len(minStr) - 1]
    return minStr


print(longestCommonPrefix2(["flower","flow","flight"]))