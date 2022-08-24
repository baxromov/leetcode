nums = [3, 2, 3, 1, 3]


# 1 Solution
# def majorityElement(nums):
#     nums.sort()
#     return nums[len(nums) // 2]


# 2 Solution
# from collections import Counter
# def majorityElement(nums):
#     d = Counter(nums)
#     f = dict()
#     for k, v in d.items():
#         f[v] = k
#     k = max(f)
#     return f[k]
#
# print(majorityElement(nums))

# 3 Solution
# n = 0
# l = None
# nums2 = list(set(nums))
# for i in nums2:
#     p = nums.count(i)
#     if p > n:
#         n = p
#         l = i
# print(l)
