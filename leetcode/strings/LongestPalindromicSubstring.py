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


def longestPalindrome(s: str) -> str:
    left, right = 0, len(s) - 1
    result = ""
    while left < right:
        if isPalindrome(s[left:right]):
            if len(result) < len(s[left:right]):
                result = s[left:right]
            left += 1
            right -= 1
        else:
            right -= 1
    return result


def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    return True


print(longestPalindrome("babad"))