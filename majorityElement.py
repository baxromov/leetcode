nums = [3, 2, 3]


def majorityElement(nums):
    nums.sort()
    return nums[len(nums) // 2]
