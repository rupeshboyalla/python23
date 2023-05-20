"""
give string (a)(a)(a) and [[a][apple]] o/p appleappleapple


"""
from typing import List
def stringReplace(s:str, target) -> str:
    lookUpMap = {}
    for ele in target:
        lookUpMap[ele[0]] = ele[1]
    for key, value in lookUpMap.items():
        if key in s:
          s=s.replace(key, value)
    s = s.replace("(","")
    s = s.replace(")", "")
    return s

print(stringReplace("(a)(b)(c)", [["a","apple"],["b","ball"],["c","cat"]]))
