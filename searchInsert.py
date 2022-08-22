nums = [1, 3, 5, 6]
target = 0


def searchInsert(nums: list, target: int):
    n = len(nums)
    if target in nums:
        return nums.index(target)
    else:
        for i in range(n - 1, -1, -1):
            if target > nums[i]:
                return i + 1
    return 0


print(searchInsert(nums, target))
