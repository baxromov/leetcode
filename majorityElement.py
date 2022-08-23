nums = [3, 2, 3]


# 1 Solution
# def majorityElement(nums):
#     nums.sort()
#     return nums[len(nums) // 2]

from collections import Counter
def majorityElement(nums):
    d = Counter(nums)
    f = dict()
    for k, v in d.items():
        f[v] = k
    k = max(f)
    return f[k]

print(majorityElement(nums))