"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
 No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true


"""

def isIsomoric(s:str, t:str):
    charHashMap = {}
    if len(s) != len(t):
        return False
    for idx, char in enumerate(s):
        if char not in charHashMap and t[idx] in charHashMap.values():
            return False
        else:
            charHashMap[char] = t[idx]
        if charHashMap[char] != t[idx]:
            return False
    return True

isIsomoric("foo", "bar")