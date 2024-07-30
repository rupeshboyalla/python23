'''
Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.



Example 1:

Input: n = 8
Output: 6
Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 is the pivot integer since: 1 = 1.
Example 3:

Input: n = 4
Output: -1
Explanation: It can be proved that no such integer exist.




'''

'''
calcualte the left sum and rightsum and check leftsum === right sum

'''

def pivotInteger(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    rightSum = sum
    leftsum = 0
    for i in range(1, n+1):
        leftsum += i
        if leftsum == rightSum:
            return i
        else:
            rightSum -= i
    return -1

'''

another approach is by taking left and right pointer 



'''
def pivotInteger2(n):
    leftSum, rightSum = 1, n
    left, right = 1, n
    if n == 1:
        return 1
    while left < right:
        if leftSum < rightSum:
            left += 1
            leftSum += left
        else:
            right -= 1
            rightSum += right
        if leftSum == rightSum and left == right:
            return left
    return -1

print(pivotInteger2(8))



