# def findRestaurant(list1, list2):
#     res = list()
#     list1_size, list2_size = len(list1), len(list2)
#     for min_sum in range(list1_size + list2_size - 1):
#         for i in range(min_sum + 1):
#             if i < list1_size and min_sum - i < list2_size and list1[i] == list2[min_sum - i]:
#                 res.append(list1[i])
#         if len(res) > 0:
#             break
#     return res



# `solution 3
# sum = len(list1)+len(list2)
# l2 = []
# k = 0
# d = None
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if list1[i] == list2[j]:
#             if i + j < sum:
#                 sum = j + i
#                 d = j
# if d != None: l2.append(list2[d])
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if list1[i] == list2[j]:
#             if i + j <= sum and l2[0] != list2[j]:
#                 sum = j + i
#                 l2.append(list2[j])
# return l2


# Solution 4



list1 = []
list2 = []

l1 = 0
l2 = 0
res = {}

for i in list1:
    if i in list2:
        l2 = list2.index(i)
        if l2 + l1 in res.values():
            res[i] = l1 + l2
        else:
            if not len(res):
                res[i] = l1 + l2
            else:
                for value , index in res.items():
                    if index > l2+l1:
                        res.clear()
                        res[i] = l1 + l2
                        break
                    else:
                        continue
    else:
        pass
    l1 += 1
print(list(res.keys()))