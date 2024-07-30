"""


Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


"""

# refer to neetcode - https://www.youtube.com/watch?v=XYQecbcd6_c

def longestPalindrome(s: str) -> str:
    result = 0
    resultLen = 0
    for i in range(len(s)):
        # odd palindrome
        left, right = i , i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left +1 > resultLen:
                result = s[left:right+1]
                resultLen = right - left +1
            left -=1
            right +=1

        left, right = i, i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left +1 > resultLen:
                result = s[left:right+1]
                resultLen = right - left +1
            left -=1
            right +=1

    return result




print(longestPalindrome("cbbd"))