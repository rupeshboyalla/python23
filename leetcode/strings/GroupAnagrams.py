"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

"""
from collections import defaultdict
from typing import List

# https://www.youtube.com/watch?v=jCZnHfDoAXE
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    lookupTable = defaultdict(list)
    for s in strs:
        key= "".join(sorted(list(s)))
        lookupTable[key].append(s)
    result = []
    for value in lookupTable.values():
        result.append(value)
    return result

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


