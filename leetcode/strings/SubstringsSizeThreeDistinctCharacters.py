"""
A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.



Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".


"""


def countGoodSubstrings(s: str, k: int) -> int:
    charVisited = set()
    left = 0
    result = 0
    for i in range(len(s)):
        while s[i] in charVisited or len(charVisited) >= k:
            charVisited.remove(s[left])
            left += 1
        charVisited.add(s[i])
        if len(charVisited) == k:
            result += 1
    return result

print(countGoodSubstrings("aababcabc", 3))


def countGoodSubstringsRupesh(s: str) -> int:
    result = 0
    left = 0
    temp = s[0]
    for i in range(1, len(s)):
        if s[left] != s[i] and len(temp) < 3:
            temp += s[i]
        elif s[left] == s[i]:
            left += 1
            temp = temp[1:]
        elif len(temp) == 3:
            temp = temp[1:]
            result += 1
    return result

print(countGoodSubstrings("aababcabc"))