from typing import List

def splitArrayInEqualParts1(nums: List[int], n: int):
    print("inside the function")
    result = []
    for i in range(0, len(nums), n):
        result.append(nums[i:i+n])
    return result

print(splitArrayInEqualParts1([1,2,3,4,5,6,7], 3))