"""
give string (a)(a)(a) and [[a][apple]] o/p appleappleapple


"""
from typing import List
def stringReplace(s:str, target) -> str:
    lookUpMap = {}
    result = ''
    for ele in target:
        lookUpMap[ele[0]] = ele[1]
    for key, value in lookUpMap.items():
        if key in s:
            result = result+lookUpMap.get(key)
    return result

print(stringReplace("(a)(b)(c)", [["a","apple"],["b","ball"],["c","cat"]]))
