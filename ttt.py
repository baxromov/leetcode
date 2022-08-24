#
#
# l = [1, 2, 3, 3, 4, 4, 5, 2]
#
# def rm_copies(_list: list) -> list:
#     res = []
#     for i in _list:
#         if i not in res:
#             res.append(i)
#     return res
#
# print(rm_copies(l))
#
#
# def sum13(nums):
#     for i in range(len(nums)):
#         if nums[i] == 13:
#             nums[i] = 0
#             if i + 1 < len(nums):
#                 nums[i + 1] = 0
#     return sum(nums)
#
#
# """
# counter = True
#
# [1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]
#                                  T
# sum = 2
# """
# def sum67(nums):
#   n = len(nums)
#   counter = True
#   summa = 0
#   for i in range(n):
#     if nums[i] == 6:
#       counter = False
#     elif counter == False and nums[i] == 7:
#       counter = True
#     elif counter:
#       summa += nums[i]
#   return summa
#
#
#
# def has22(nums):
#   n = len(nums)
#   for i in range(n - 1):
#     if nums[i] == 2 and nums[i+1] == 2:
#       return True
#   return False
#
#
# print(has22([1,2,2]))
#
#
from functools import reduce

a = [1, 2, 3, 4, 5, 6, 7]
d = reduce(lambda x, y: x - y, a)

# ((((((1 + 2) + 3)) + 4) + 5) + 6) + 7
