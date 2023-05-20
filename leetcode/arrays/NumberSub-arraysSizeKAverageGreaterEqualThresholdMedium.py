"""
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.



Example 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
Example 2:

Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.

https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/


"""

from typing import List

def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    left = 0
    window = []
    result = 0
    currSum = 0
    for i in range(len(arr)):
        currSum += arr[i]
        window.append(arr[i])
        if len(window) == k:
            if (currSum // k) >= threshold:
                result += 1
            currSum -= arr[left]
            window.remove(arr[left])
            left += 1
    return result

print(numOfSubarrays([11,13,17,23,29,31,7,5,2,3], 3, 5))



