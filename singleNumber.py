from typing import List



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


# 4 Solutionclass
# Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         a = 0
#         for i in nums:
#             a = i ^ a
#         return a

# 5 Solution
# nums = [1,1,2,2,4]
# nums.sort()
# b = None
# for i in nums:
#     if b != i and nums.count(i) == 1:
#         print(i)
#         break
#     b = i
# print(b)