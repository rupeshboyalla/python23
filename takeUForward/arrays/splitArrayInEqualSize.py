
'''

Split the array in equal size

yield


'''

from typing import List
def splitArrayInEqualParts(nums:List[int], n:int):
    result = []
    print("inside an array")
    for i in range(0, len(nums), n):
        yield result[i:i+n]
    return result

print(splitArrayInEqualParts([1,2,3,4,5,6,7], 2))
