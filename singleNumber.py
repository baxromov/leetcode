from typing import List

nums = [4, 1, 2, 1, 2]


# 1 Solution
# def singleNumber(nums: List[int]) -> int:
#     return 2 * sum(set(nums)) - sum(nums)

# 2 Solution
# from collections import Counter
# def singleNumber(nums: list):
#     d = Counter(nums)
#     f = dict()
#     for k, v in d.items():
#         f[v] = k
#     k = min(f)
#     return f.get(k)


# 3 Solution
# correct way but Time Limit Exceeded
# def singleNumber(nums: list):
#     return tuple(filter(lambda x: nums.count(x) == 1, tuple(nums)))[0]
# print(singleNumber(nums))