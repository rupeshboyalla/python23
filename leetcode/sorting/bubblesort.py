


def bubbleSort(nums):
    for i in range(len(nums)):
        for j in reversed(range(i+1, len(nums))):
            if nums[j] < nums[j-1]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
    return nums

print(bubbleSort( [5, 3, 1, -10, -11, -100]))