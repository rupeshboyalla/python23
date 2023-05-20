"""

Given a string s and an integer k, return the number of substrings in s of length k with no repeated characters.



Example 1:

Input: s = "havefunonleetcode", k = 5
Output: 6
Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: s = "home", k = 5
Output: 0
Explanation: Notice k can be larger than the length of s. In this case, it is not possible to find any substring.




https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/


"""

def numKLenSubstrNoRepeats(s: str, k: int) -> int:
    charVisited = set()
    left = 0
    result = 0
    for right in range(len(s)):
        while s[right] in charVisited or len(charVisited) >= k:
            charVisited.remove(s[left])
            left += 1
        charVisited.add(s[right])
        if len(charVisited) == k:
            result += 1
    return result
print(numKLenSubstrNoRepeats("havefunonleetcode", 5))