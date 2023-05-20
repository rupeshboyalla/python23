"""
Given a string s, return true if a permutation of the string could form a
palindrome
 and false otherwise.



Example 1:

Input: s = "code"
Output: false
Example 2:

Input: s = "aab"
Output: true
Example 3:

Input: s = "carerac"
Output: true

"""


def canPermutePalindrome(s: str) -> bool:
    lookupTable = {}
    countOdd = len(s) % 2
    for char in s:
        lookupTable[char] = 1 + lookupTable.get(char, 0)
    count = 0
    for value in lookupTable.values():
        if value % 2 != 0:
            count += 1
    return count == countOdd
print(canPermutePalindrome("aab"))
