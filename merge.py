# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
#
#
# # 1 solution
# def merge1(nums1: list, m: int, nums2: list, n: int):
#     i, j, k = 0, 0, 0
#     temp = nums1.copy()
#     while i < m and j < n:
#         if temp[k] < nums2[j]:
#             nums1[k] = temp[i]
#             i += 1
#         else:
#             nums1[k] = nums2[j]
#             j += 1
#         k += 1
#
#     while i < m:
#         nums1[k] = temp[i]
#         i += 1
#         k += 1
#     while j < n:
#         nums1[k] = nums2[j]
#         j += 1
#         k += 1
#
#
# # 2 solution
# def merge(nums1: list, m: int, nums2: list, n: int):
#     nums1[len(nums1) - n:] = nums2
#     nums1.sort()
#
#
# print(nums1)
# merge(nums1, m,nums2,n )
# print(nums1)
#
#
# def merge(self, nums1: int, m: int, nums2: int, n: int) -> None:
#     """
#     Do not return anything, modify nums1 in-place instead.
#     """
#     i = 0
#     while i < len(nums1):
#         if nums1.count(0) and len(nums2) > 0:
#             indexx = nums1.index(0)
#             nums1[indexx] = nums2[0]
#             nums2.pop(0)
#         i += 1
#     nums1.sort()
#
#
#
#
#
#
#
#
#
#
#
#
#
# """
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
#
# nums1[m] =
# """
#
#
#
#
#
#
#
