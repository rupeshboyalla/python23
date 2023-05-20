def reverseList(nums: int, start, end):
    if start > end:
        print(nums)
        return
    nums[start], nums[end] = nums[end], nums[start]
    reverseList(nums, start+1, end-1)


reverseList([3,2,1,4,5], 0, len([3,2,1,4,5])-1)