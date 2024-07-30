"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false




"""
from typing import List

def isAnagram(s: str, t: str) -> bool:
    lookupTable = {}
    for char in s:
        lookupTable[char] = 1+lookupTable.get(char, 0)
    for char in t:
        if char in lookupTable and lookupTable[char] != 0:
            lookupTable[char] = lookupTable.get(char) - 1
        else:
            return False
    return True

print(isAnagram("anagram", "nagaram"))
